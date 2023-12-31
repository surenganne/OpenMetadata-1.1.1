---
title: tag
slug: /main-concepts/metadata-standard/schemas/entity/classification/tag
---

# Tag

*A `Tag` entity is used for classification or categorization. It is a term defined under `Classification` entity. Tags are used to label the entities and entity fields, such as Tables, and Columns.*

## Properties

- **`id`**: Unique identifier of this entity instance. Refer to *../../type/basic.json#/definitions/uuid*.
- **`name`**: Name of the tag. Refer to *#/definitions/tagName*.
- **`displayName`** *(string)*: Display Name that identifies this tag.
- **`fullyQualifiedName`** *(string)*: Unique name of the tag of format `Classification.tag1.tag2`.
- **`description`**: Description of the tag. Refer to *../../type/basic.json#/definitions/markdown*.
- **`classification`**: Reference to the classification that this tag is part of. Refer to *../../type/entityReference.json*.
- **`parent`**: Reference to the parent tag. When null, the term is at the root of the Classification. Refer to *../../type/entityReference.json*.
- **`children`**: Children tags under this tag. Refer to *../../type/entityReferenceList.json#/definitions/entityReferenceList*.
- **`version`**: Metadata version of the entity. Refer to *../../type/entityHistory.json#/definitions/entityVersion*.
- **`updatedAt`**: Last update time corresponding to the new version of the entity in Unix epoch time milliseconds. Refer to *../../type/basic.json#/definitions/timestamp*.
- **`updatedBy`** *(string)*: User who made the update.
- **`href`**: Link to the resource corresponding to the tag. Refer to *../../type/basic.json#/definitions/href*.
- **`usageCount`** *(integer)*: Count of how many times this tag and children tags are used.
- **`deprecated`** *(boolean)*: If the tag is deprecated. Default: `False`.
- **`deleted`** *(boolean)*: When `true` indicates the entity has been soft deleted. Default: `False`.
- **`changeDescription`**: Change that lead to this version of the entity. Refer to *../../type/entityHistory.json#/definitions/changeDescription*.
- **`provider`**: Refer to *../../type/basic.json#/definitions/providerType*.
- **`disabled`** *(boolean)*: System tags can't be deleted. Use this flag to disable them.
- **`mutuallyExclusive`** *(boolean)*: Children tags under this group are mutually exclusive. When mutually exclusive is `true` the tags from this group are used to **classify** an entity. An entity can only be in one class - example, it can only be either `tier1` or `tier2` and not both. When mutually exclusive is `false`, the tags from this group are used to **categorize** an entity. An entity can be in multiple categories simultaneously - example a customer can be `newCustomer` and `atRisk` simultaneously. Default: `false`.
## Definitions

- **`tagName`** *(string)*: Name of the tag.


Documentation file automatically generated at 2023-07-07 05:50:35.981927.
