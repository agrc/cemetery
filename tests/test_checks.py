#!/usr/bin/env python
# * coding: utf8 *
"""
test_checks.py
A module that contains tests for the checks module.
"""

import psycopg2
import pytest

from conductor.checks import (
    ArcGisOnlineChecker, MetaTableChecker, MSSqlTableChecker, OpenDataChecker, PGSqlTableChecker, TableChecker
)

try:
    from conductor.connections import DB
except ModuleNotFoundError:
    from conductor.connection_sample import DB

CONNECTION_STRING = ''


def test_imports():
    assert True


def test_checker_raises_for_table_without_schema():
    with pytest.raises(ValueError):
        table = 'city'
        TableChecker(table, CONNECTION_STRING)


def test_checker_parses_table_with_schema():
    table = 'location.city'
    patient = TableChecker(table, CONNECTION_STRING)

    assert patient.table == 'city'
    assert patient.schema == 'location'


def test_checker_parses_table_with_schema_and_db():
    table = 'dbo.location.city'
    patient = TableChecker(table, CONNECTION_STRING)

    assert patient.table == 'city'
    assert patient.schema == 'location'


def test_checker_raises_with_too_many_parts():
    table = 'some.very.long.table.name'

    with pytest.raises(ValueError):
        TableChecker(table, CONNECTION_STRING)


def test_checker_raises_with_empty_connection_string():
    with pytest.raises(ValueError):
        TableChecker('schema.table', '').connect()


def test_checker_raises_with_no_connection_string():
    with pytest.raises(ValueError):
        TableChecker('schema.table', None).connect()


def test_open_sgid_can_connect():
    patient = PGSqlTableChecker('boundaries.municipal_boundaries', DB['opensgid'])

    cursor = patient.connect()

    assert cursor.connection.status == psycopg2.extensions.STATUS_READY

    cursor.close()
    patient.connection.close()


@pytest.mark.vpn
def test_mssql_table_can_connect():
    patient = MSSqlTableChecker('boundaries.municipalities', DB['sgid10'])

    cursor = patient.connect()

    assert cursor is not None


def test_pgsql_table_exists_returns_true():
    patient = PGSqlTableChecker('boundaries.municipal_boundaries', DB['opensgid'])

    assert patient.exists() == True

    patient.connection.close()


@pytest.mark.vpn
def test_mssql_table_exists_returns_true():
    patient = MSSqlTableChecker('boundaries.municipalities', DB['sgid10'])

    assert patient.exists() == True

    patient.connection.close()


def test_pgsql_table_does_not_exist_returns_false():
    patient = PGSqlTableChecker('fake.table', DB['opensgid'])

    assert patient.exists() == False

    patient.connection.close()


@pytest.mark.vpn
def test_mssql_table_does_not_exist_returns_false():
    patient = MSSqlTableChecker('fake.table', DB['sgid10'])

    assert patient.exists() == False

    patient.connection.close()


@pytest.mark.vpn
def test_metatable_response_returns_true_when_exists():
    patient = MetaTableChecker('sgid.boundaries.municipalities', DB['internalsgid'])
    response = patient.exists()

    assert response == True
    assert patient.data.item_id == '543fa1f073714198a3dbf8a292bdf30c'
    assert patient.data.item_name == 'Utah Municipal Boundaries'


@pytest.mark.vpn
def test_response_returns_completely_missing_for_fake_table():
    patient = MetaTableChecker('sgid.fake.table', DB['internalsgid'])
    response = patient.exists()

    assert response == False


def test_empty_row_returns_false(mocker):
    mocker.patch('conductor.checks.TableChecker.get_data')

    patient = MetaTableChecker('sgid.fake.table', DB['internalsgid'])
    response = patient.exists()

    assert response == False


def test_missing_item_id_returns_correct_string(mocker):
    mocker.patch('conductor.checks.TableChecker.get_data')

    patient = MetaTableChecker('sgid.fake.table', DB['internalsgid'])
    patient.data = (None, 'Agol Published Name')

    response = patient.exists()

    assert response == 'missing item id'


def test_missing_item_name_returns_correct_string(mocker):
    mocker.patch('conductor.checks.TableChecker.get_data')

    patient = MetaTableChecker('sgid.fake.table', DB['internalsgid'])
    patient.data = ('some-guid', None)

    response = patient.exists()

    assert response == 'missing item name'


def test_missing_both_returns_correct_string(mocker):
    mocker.patch('conductor.checks.TableChecker.get_data')

    patient = MetaTableChecker('sgid.fake.table', DB['internalsgid'])
    patient.data = (None, None)

    response = patient.exists()

    assert response == False


def test_arcgis_online_url_creation():
    patient = ArcGisOnlineChecker('item_id')

    assert patient.url == 'https://www.arcgis.com/sharing/rest/content/items/item_id'


def test_arcgis_online_exists_when_json_contains_owner(mocker):
    mocker.patch('conductor.checks.UrlChecker.get_data')
    patient = ArcGisOnlineChecker('item_id')
    patient.data = mocker.Mock(
        **{
            'json.return_value': {
                "id": "3080c0a2859a4d23a279e17e17c703c8",
                "owner": "UtahAGRC",
                "orgId": "123",
                "created": 1593230216000,
                "modified": 1594153455000,
                "guid": None,
                "name": "TrailsAndPathways",
                "title": "Utah Trails and Pathways",
                "type": "Feature Service"
            }
        }
    )

    assert patient.exists() == True


def test_arcgis_online_does_not_exist(mocker):
    mocker.patch('conductor.checks.ArcGisOnlineChecker.get_data')
    patient = ArcGisOnlineChecker('item_id')
    patient.data = mocker.Mock(
        **{
            'json.return_value': {
                "error": {
                    "code": 400,
                    "messageCode": "CONT_0001",
                    "message": "Item does not exist or is inaccessible.",
                    "details": []
                }
            }
        }
    )

    assert patient.exists() == False


def test_open_data_url_creation():
    patient = OpenDataChecker('UPPER CASED Name')

    assert patient.url == 'https://opendata.gis.utah.gov/datasets/upper-cased-name'


def test_open_data_for_existence_with_200(mocker):
    mocker.patch('conductor.checks.UrlChecker.get_data')

    patient = OpenDataChecker('found layer name')
    patient.data = mocker.Mock()
    patient.data.status_code = 200

    assert patient.exists() == True


def test_open_data_for_missing_with_301(mocker):
    mocker.patch('conductor.checks.UrlChecker.get_data')

    patient = OpenDataChecker('missing layer name')
    patient.data = mocker.Mock()
    patient.data.status_code = 301

    assert patient.exists() == False
