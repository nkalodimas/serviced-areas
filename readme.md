This web application was built using Django Framework, PostgreSql with the use of PostGIS, in order to enable the use of location queries, GoogleMaps API and JQuery.
It is hosted on an Amazon EC2 server and you can access it on the following url:

http://ec2-54-213-202-239.us-west-2.compute.amazonaws.com:8000/areas/

It consists of 2 web pages:
1)
http://ec2-54-213-202-239.us-west-2.compute.amazonaws.com:8000/areas/create
and

2)
http://ec2-54-213-202-239.us-west-2.compute.amazonaws.com:8000/areas/check

Through the first page a user can see a Google Maps map and can draw a polygon
that represents the area for which he can provide his services.
After drawing the polygon the user can also modifie it and afterwards can submit
the area.
The coordinates of the last submitted area are displayed on the top of the page.
The clear button does not function properly yet.
The user can submit multiple areas, one at a time.

Through the second page the user can check if a single point, that he pins on the map
belongs to a serviced area that has previusly been submitted.
When the user pins the mapper a flash message appears on the top of the screen and the
mapper's colour also changes according to the result.
If the point is serviced it becomes green and if not it becomes purple.
The user can pin multiple points and view them all inside the map.

---------------------------------------------------------------------------------------
API documentation
---------------------------------------------------------------------------------------

**Submit an Area**
----
  Returns only status.

* **URL**

  /areas/submit

* **Method:**

  `POST`
  
*  **Data Params**

   **Required:**
 
   `json dictionary with key='points' and value=list of objects of type:{'lat':value , 'long':value}`
   example: { 'points' : [{lat: 25.774, lng: -80.190},{lat: 18.466, lng: -66.118},{lat: 32.321, lng: -64.757},{lat: 25.774, lng: -80.190}] }

* **Url Params**

  None

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** None
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />

* **Sample Call:**

  ```javascript
    $.ajax({
			url  : 'submit/',
			type : 'POST',
			data : JSON.stringify({"points" : points })
			})
  ```

**Search for an Area**
----
  Returns only status.

* **URL**

  /areas/search

* **Method:**

  `GET`
  
*  **Data Params**

  None

* **Url Params**

  **Required:**

  `lat=[float]`
  `lng=[float]`

* **Success Response:**

  * **Code:** 200 <br />
    **When:** Found

  OR

  * **Code:** 204 <br />
    **When:** Not found
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />

* **Sample Call:**

  ```javascript
    $.ajax({
			url  : 'search/',
			type : 'GET',
			data : {"lat" : location.lat(),"lng" : location.lng()}
			})
  ```
