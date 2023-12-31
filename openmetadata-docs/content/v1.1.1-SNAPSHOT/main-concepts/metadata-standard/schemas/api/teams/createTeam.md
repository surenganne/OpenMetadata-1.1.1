---
title: createTeam
slug: /main-concepts/metadata-standard/schemas/api/teams/createteam
---

# CreateTeamRequest

*Team entity*

## Properties

- **`teamType`**: Team type. Refer to *../../entity/teams/team.json#/definitions/teamType*.
- **`name`**: Refer to *../../type/basic.json#/definitions/entityName*.
- **`email`**: Email address of the team. Refer to *../../type/basic.json#/definitions/email*.
- **`displayName`** *(string)*: Optional name used for display purposes. Example 'Marketing Team'.
- **`description`**: Optional description of the team. Refer to *../../type/basic.json#/definitions/markdown*.
- **`profile`**: Optional team profile information. Refer to *../../type/profile.json*.
- **`parents`** *(array)*: Parent teams. For an `Organization` the `parent` is always null. A `BusinessUnit` always has only one parent of type `BusinessUnit` or an `Organization`. A `Division` can have multiple parents of type `BusinessUnit` or `Division`. A `Department` can have multiple parents of type `Division` or `Department`. Default: `None`.
  - **Items**: Refer to *../../type/basic.json#/definitions/uuid*.
- **`children`** *(array)*: Children teams. An `Organization` can have `BusinessUnit`, `Division` or `Department` as children. A `BusinessUnit` can have `BusinessUnit`, `Division`, or `Department` as children. A `Division` can have `Division` or `Department` as children. A `Department` can have can have `Department` as children. Default: `None`.
  - **Items**: Refer to *../../type/basic.json#/definitions/uuid*.
- **`users`** *(array)*: Optional IDs of users that are part of the team. Default: `None`.
  - **Items**: Refer to *../../type/basic.json#/definitions/uuid*.
- **`defaultRoles`** *(array)*: Roles to be assigned to all users that are part of this team. Default: `None`.
  - **Items**: Refer to *../../type/basic.json#/definitions/uuid*.
- **`owner`**: Owner of this team. . Refer to *../../type/entityReference.json*. Default: `None`.
- **`isJoinable`** *(boolean)*: Can any user join this team during sign up? Value of true indicates yes, and false no. Default: `True`.
- **`policies`** *(array)*: Policies that is attached to this team. Default: `None`.
  - **Items**: Refer to *../../type/basic.json#/definitions/uuid*.
- **`domain`** *(string)*: Fully qualified name of the domain the Team belongs to.


Documentation file automatically generated at 2023-07-07 05:50:35.981927.
