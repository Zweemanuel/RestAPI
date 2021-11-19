# REST API
## CREATE
Endpoint that allows to insert a city to the city table.
Done so in a POST request.
API response is the created record in the database.

## READ
Endpoint that returns the details of a city (Name, Country, District, Population count) 
Done by passing the name of a city is as input to the service. API response is the retrieved record from the database.

## UPDATE
Endpoint that updates the population count of a city stored in the database.
API response is the modified database record.

## DELETE
Endpoint that deletes a city from the database.
API response is a boolean: true if the record was successfully deleted or false otherwise
