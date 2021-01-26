---
name: Removing an application
about: Application Checklist
title: Deprecate <application>
labels: "deprecation, porter"
assignees: "@steveoh, @gregbunce, @rkelson"
---

# Summary

- **Application Name**:
- **Application Url**:

_A short summary of the situation._

## Action items

1. _Assign a person who should complete the task by replacing `name` with their github `@name`._
1. _Check [x] the box when the task is completed and add the date of completion._
1. _~Strike~ out all items that do not apply._

- [ ] Update relevant [gis.utah.gov](https://gis.utah.gov/developer/application) application pages (name, completed: `2021/00/00`)
- [ ] Remove forklift pallet (name, completed: `2021/00/00`)
- [ ] Remove application-specific Databases (name, completed: `2021/00/00`)
- [ ] AGRC Projects team drive [folder](https://drive.google.com/drive/folders/0AIVByxAYHd4oUk9PVA) (name, completed: `2021/00/00`)

### Is there a website?

- [ ] Remove DNS entry (name, completed: `2021/00/00`)
- [ ] Archive source code repository (name, completed: `2021/00/00`)

_Choose one._

- [ ] Remove from the web server (name, completed: `2021/00/00`)
- [ ] Replace app with a static page with information (name, completed: `2021/00/00`)
- [ ] Redirect somewhere else (name, completed: `2021/00/00`)

### Is there a map service?

- [ ] Stop (name, completed: `2021/00/00`)
- [ ] Delete (name, completed: `2021/00/00`)

### Is there a forklift pallet?

- [ ] Remove repo (name, completed: `2021/00/00`)
- [ ] Remove stale data from forklift hashing and receiving (name, completed: `2021/00/00`)
- [ ] Remove row from `data/hashed/changedetection.gdb/TableHashes` (name, completed: `2021/00/00`)

### Are there service dependencies?

- [ ] Validate that the web api does not query it (name, completed: `2021/00/00`)
- [ ] Validate that AGRC or applications widgets do not reference it (name, completed: `2021/00/00`)

## Notification

- [ ] Twitter (@steveoh)

## Group Task Assignments

1. _Check [x] the box when you have assigned all the tasks relevant to your group._

- [ ] Data Team (@gregbunce)
- [ ] Dev Team (@steveoh)
- [ ] Cadastre Team (@rkelson)
