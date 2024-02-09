## Contributors

-Zaquari Andl

## Description

- An app that will show farms and their workers, animals, and will allow you to alter who and what is  inside of the farm. 

## Github Repo

- https://github.com/ZaquariA/Phase-4-Project

## DB Diagram

![diagramERD](https://i.imgur.com/AKc9kuX.png)
https://dbdiagram.io/d/65c51ea2ac844320aec2690f

## CRUD

-Create a farm, farmer, or animal

-Read all farms that allow you to see each name of farmers and what type of farm and when clicked, you're able to see those farmers and animals in detail

-Update the names of the animals, farmers, and farms

-Delete the farms, animals, and farmers based on wether you're wanting to remove them

## MODELS
many-to-many relationship
A Farmer has many Animals through Farms
A Animal has many Farmers through Farms
A Farm belongs to a Farmer and belongs to an Animal

## Validations

- Validations for Farmer:
- - must have a name
- - must have an age between 18 and 65
- - must have a gender
- - must have an image url
- Validations for Animal:
- -  must have a name
- - must have a breed
- - must have an image url
** Stretch **
- - must have a feed for each animal
- Validations for Farm:
- - must have a size 
- - must have a date of establishment


## CONTROLLERS

***​​API routes RESTful conventions***
>
## Animals

GET /animals/

POST /animals/
>

GET /animals/<int:id>

PATCH /animals/<int:id>

DELETE /animals/<int:id>
>

## Farmers

GET /farmers/

POST /farmers/
>
GET /farmers/<int:id>

PATCH /farmers/<int:id>

DELETE /farmers/<int:id>
>
## Farms

GET /farms/

POST /farms/

>
GET /farms/<int:id>

PATCH /farms/<int:id>

DELETE /farms/<int:id>
