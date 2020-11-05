from flask import Flask,request,jsonify,make_response
from datetime import datetime
import db
from flasgger import Swagger

app = Flask(__name__)

template = {
  "swagger": "2.0",
  "info": {
    "title": "My API",
    "description": "API for my data",
    "contact": {
      "responsibleOrganization": "ME",
      "responsibleDeveloper": "Me",
      "email": "me@me.com",
      "url": "www.me.com",
    },
    "termsOfService": "http://me.com/terms",
    "version": "1"
  },
}

swagger = Swagger(app, template=template)


# Add Device
@app.route('/addDevice', methods=['POST'])
def addDevice():

    """ Call to Add Device
    ---
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
            required:
              - device_id
              - device_name
              - vendor
              - created_at
              - is_device_in_hub
              - created_at_hub
            properties:
                device_id:
                    type: number
                    example: 1
                device_name:
                    type: string
                    example: "tk259"
                vendor:
                    type: string
                    description: "asasd"
                    example: "Ishfaq"
                created_at:
                    type: string
                    example: "29-03-2013 15:59:02"
                is_device_in_hub:
                    type: boolean
                    example: true
                created_at_hub:
                    type: string
                    example: "29-03-2013 15:59:02"
    responses:
        200:
            description: "Device is insesrt successfully"
            msg: string
            code: number
        409:
            description: "Device with same device_id exists."
            msg: string
            code: number
        400: 
            description: "Database Connection error OR Bad Request."
            msg: string
            code: number
    """

    if request.is_json:
        req = request.get_json()
        result = db.addDevice(req)
        
        if result == 200:
            response = {
                'message': 'OK'
            }
        
            json_response = make_response(jsonify(response))
            return json_response,200
        elif result == 409:
            response = {
                'message': 'Device with same device_id exists.'
            }
        
            json_response = make_response(jsonify(response))
            return json_response,409
        elif result == 400:
            response = {
                'message': 'Database Connection error.'
            }
        
            json_response = make_response(jsonify(response))
            return json_response,400
        
    else:
        response = {
                'message': 'Bad Request.'
            }
        json_response = make_response(jsonify(response))
        return json_response,400

# Add User
@app.route('/addUser', methods=['POST'])
def addUser():

    """ Call to Add User
    ---
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
            required:
              - user_id
              - user_name
              - address
              - dob
              - created_at
            properties:
                user_id:
                    type: number
                    example: 1
                user_name:
                    type: string
                    example: "user_1"
                address:
                    type: string
                    exmaple: "kalma chowk"
                created_at:
                    type: string
                    example: "29-03-2013 15:59:02"
                dob:
                    type: string
                    example: "29-03-1991"
                created_at_hub:
                    type: string
                    example: "29-03-2013 15:59:02"
    responses:
        200:
            description: "User is insesrt successfully"
            msg: string
            code: number
        409:
            description: "User with same user_id exists."
            msg: string
            code: number
        400: 
            description: "Database Connection error OR Bad Request."
            msg: string
            code: number
    """

    if request.is_json:
        req = request.get_json()
        result = db.addUser(req)
        
        if result == 200:
            response = {
                'message': 'OK'
            }
        
            json_response = make_response(jsonify(response))
            return json_response,200
        if result == 409:
            response = {
                'message': 'User with same user_id exists.'
            }
        
            json_response = make_response(jsonify(response))
            return json_response,409
        elif result == 400:
            response = {
                'message': 'Database Connection error.'
            }
        
            json_response = make_response(jsonify(response))
            return json_response,400
        
    else:
        response = {
                'message': 'Bad Request.'
            }
        json_response = make_response(jsonify(response))
        return json_response,400

# Modify Device
@app.route('/modifyDevice', methods=['POST'])
def modifyDevice():

    """ Call to Modify Device
    ---
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
            required:
              - device_id
              - device_name
              - vendor
              - created_at
              - is_device_in_hub
              - created_at_hub
            properties:
                device_id:
                    type: number
                    example: 1
                device_name:
                    type: string
                    example: "tk259"
                vendor:
                    type: string
                    description: "asasd"
                    example: "Ishfaq"
                created_at:
                    type: string
                    example: "29-03-2013 15:59:02"
                is_device_in_hub:
                    type: boolean
                    example: true
                created_at_hub:
                    type: string
                    example: "29-03-2013 15:59:02"
    responses:
        200:
            description: "Device is modified successfully"
            msg: string
            code: number
        400: 
            description: "Please Provide all required fields or Database Connection error or Bad Request"
            msg: string
            code: number
        409:
            description: "Device with this device_id does not exits."
            msg: string
            code: number        
    """

    if request.is_json:
        req = request.get_json()
        
        if 'device_id' not in req or 'device_name' not in req:
            response = {
                'message': 'Please provide all required field.'
            }
            json_response = make_response(jsonify(response))
            return json_response,400

        else: 
            result = db.modifyDevice(req)
        
            if result == 200:
                response = {
                    'message': 'OK'
                }
                json_response = make_response(jsonify(response))
                return json_response,200
            elif result == 409:
                response = {
                    'message': 'Device with this device_id does not exits.'
                } 
                json_response = make_response(jsonify(response))
                return json_response,409
            elif result == 400:
                response = {
                    'message': 'Database Connection error.'
                } 
                json_response = make_response(jsonify(response))
                return json_response,400
            
    else:
        response = {
                'message': 'Bad Request.'
            }
        json_response = make_response(jsonify(response))
        return json_response,400

# Modify User
@app.route('/modifyUser', methods=['POST'])
def modifyUser():

    """ Call to Modify User
    ---
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
            required:
              - user_id
              - user_name
              - address
              - dob
              - created_at
            properties:
                user_id:
                    type: number
                    example: 1
                user_name:
                    type: string
                    example: "user_1"
                address:
                    type: string
                    exmaple: "kalma chowk"
                created_at:
                    type: string
                    example: "29-03-2013 15:59:02"
                dob:
                    type: string
                    example: "29-03-1991"
                created_at_hub:
                    type: string
                    example: "29-03-2013 15:59:02"
    responses:
        200:
            description: "User is modified successfully"
            msg: string
            code: number
        400: 
            description: "Please Provide all required fields or Database Connection error or Bad Request"
            msg: string
            code: number
        409:
            description: "Device with this user_id does not exits."
            msg: string
            code: number 
    """
    if request.is_json:
        req = request.get_json()
        
        if 'user_id' not in req or 'user_name' not in req:
            response = {
                'message': 'Please provide all required field.'
            }
            json_response = make_response(jsonify(response))
            return json_response,400

        else: 
            result = db.modifyUser(req)
        
            if result == 200:
                response = {
                    'message': 'OK'
                }
                json_response = make_response(jsonify(response))
                return json_response,200
            
            elif result == 409:
                response = {
                'message': 'Device with this user_id does not exits.'
                } 
                json_response = make_response(jsonify(response))
                return json_response,409
            elif result == 400:
                response = {
                'message': 'Database Connection error.'
                } 
                json_response = make_response(jsonify(response))
                return json_response,400
    else:
        response = {
                'message': 'Bad Request.'
            }
        json_response = make_response(jsonify(response))
        return json_response,400

# Rent Device
@app.route('/rentDevice', methods=['POST'])
def rentDevice():
    
    """ Call to Modify User
    ---
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
            required:
              - device_id
              - rented_at
              - rented_to_uid
              - rented_to_name
              - transaction_id
              - is_returned
              - returned_at
            properties:
                device_id:
                    type: number
                    example: 1
                rented_at:
                    type: string
                    example: "29-03-2013 15:59:02"
                rented_to_uid:
                    type: number
                    exmaple: 1
                rented_to_name:
                    type: string
                    example: "User_123"
                transaction_id:
                    type: number
                    example: "1"
                is_returned:
                    type: boolean
                    example: false
                returned_at:
                    type: string
                    example: "29-03-2013 15:59:02"
    responses:
        200:
            description: "User is modified successfully"
            msg: string
            code: number
        400: 
            description: "Database Connection error or Bad Request"
            msg: string
            code: number
        409:
            description: "device_id or user_id does not exist."
            msg: string
            code: number 
    """

    if request.is_json:
        req = request.get_json()
        
        result = db.rentDevice(req)
        
        if result == 200:
            response = {
                'message': 'OK'
            }
            json_response = make_response(jsonify(response))
            return json_response,200
        elif result == 409:
            response = {
                'message': 'device_id or user_id does not exist.'
            }
            json_response = make_response(jsonify(response))
            return json_response,409
        elif result == 400:
                response = {
                'message': 'Database Connection error.'
                } 
                json_response = make_response(jsonify(response))
                return json_response,400
    else:
        response = {
                'message': 'Bad Request.'
            }
        json_response = make_response(jsonify(response))
        return json_response,400

# Return Device
@app.route('/returnDevice', methods=['POST'])
def returnDevice():


    """ Call to Modify User
    ---
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
            required:
              - device_id
            properties:
                device_id:
                    type: number
                    example: 1
    responses:
        200:
            description: "is_returned set to true."
            msg: string
            code: number
        400: 
            description: "Database Connection error or Bad Request"
            msg: string
            code: number
        409:
            description: "Device was not rented."
            msg: string
            code: number 
    """

    if request.is_json:
        req = request.get_json()
        print("asdasd")
        result = db.returnDevice(req)
        
        if result == 200:
            response = {
                'message': 'OK'
            }

            json_response = make_response(jsonify(response))
            return json_response,200
        elif result == 409:
            response = {
                'message': 'Device was not rented.'
            }

            json_response = make_response(jsonify(response))
            return json_response,409
            
        elif result == 400:
            response = {
                'message': 'Database Connection error.'
            }
            json_response = make_response(jsonify(response))
            return json_response,400

    else:
        response = {
                'message': 'Wrong Request.'
            }
        json_response = make_response(jsonify(response))
        return json_response,400

if __name__ == '__main__':
    app.run(debug=True)


