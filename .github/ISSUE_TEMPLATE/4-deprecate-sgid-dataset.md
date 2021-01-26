---
name: Removing data from the SGID
about: SGID Deprecation Checklist
title: Remove <dataset name> from SGID
labels: "deprecation, porter"
assignees: "@steveoh, @gregbunce, @rkelson"
---

# Summary

- **Internal Dataset Name**:
- **External Dataset Name**:
- **ArcGIS Online Url**:

_A short summary of the situation._

## Action items

1. _Assign a person who should complete the task by replacing `name` with their github `@name`._
1. _Check [x] the box when the task is completed and add the date of completion._
1. _~Strike~ out all items that do not apply._

- [ ] Remove data from the Internal SGID (name, completed: `2021/00/00`)
- [ ] Delete ArcGIS Online item (name, completed: `2021/00/00`)
  - [ ] Add `deprecated` tag to ArcGIS Online item (name, completed: `2021/00/00`)
  - [ ] Add `Deprecated` to ArcGIS Online item title(name, completed: `2021/00/00`)
- [ ] Unshare item from Open Data (name, completed: `2021/00/00`)
- [ ] Remove Farm from AGOL connection (name, completed: `2021/00/00`)
- [ ] Update relevant [gis.utah.gov](https://gis.utah.gov/data) data pages (name, completed: `2021/00/00`)
- [ ] Add this porter url to the `Deprecated` field of the [Stewardship](https://docs.google.com/spreadsheets/d/11ASS7LnxgpnD0jN4utzklREgMf1pcvYjcXcIcESHweQ/edit#gid=1) record (name, completed: `2021/00/00`)
- [ ] Update `SGID.META.AGOLItems` table (name, completed: `2021/00/00`)
  - delete row if removing from both
  - set the `AGOL_ITEM_ID` field to `hosted by <agency>` for Farm from AGOL
  - set the `AGOL_ITEM_ID` field to `exclude from AGOL` to not publish to ArcGIS Online
- [ ] Delete Google Drive data (name, completed: `2021/00/00`)
- [ ] Remove row from `SGID.META.ChangeDetection` (name, completed: `2021/00/00`)
- [ ] Remove json file from [Backseat Driver](https://github.com/agrc/backseat-driver) (name, completed `2021/00/00`)
- [ ] Remove data from forklift hashing and receiving (name, completed: `2021/00/00`)
- [ ] Remove row from `data/hashed/changedetection.gdb/TableHashes` (name, completed: `2021/00/00`)

### Shelve/Static

_Choose one._

- [ ] Upload to `UtahAGRC/AGRC_Shelved` folder in AGOL (name, completed: `2021/00/00`)
- [ ] Move existing AGOL item to `AGRC_Shelved` AGOL folder (name, completed: `2021/00/00`)
- [ ] Upload to appropriate `UtahAGRC/{SGID Category}` folder in AGOL (for `static` datasets) (name, completed: `2021/00/00`)

## :robot: Automation validation

1. _Assign yourself or someone to check the item by replacing `name` with their github `@name`._
1. _Check [x] the box and add the date of verification `2020/01/01` when the task is verified._
1. _~Strike~ out all items that do not apply._

- [ ] Remove data from Open SGID (name on `2021/00/00`)
- [ ] [sgid-index](https://gis.utah.gov/data/sgid-index) (@steveoh on `2021/00/00`)

## Are there service dependencies

- Does an application depend on this data?
- Are clients querying this data with the WebAPI?

## Notification

- [ ] Twitter (@steveoh)

## Group Task Assignments

1. _Check [x] the box when you have assigned all the tasks relevant to your group._

- [ ] Data Team (@gregbunce)
- [ ] Dev Team (@steveoh)
- [ ] Cadastre Team (@rkelson)
