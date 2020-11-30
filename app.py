from flask import Flask, jsonify, request

app = Flask(__name__)

from appointments import appointments


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

# Get 
@app.route('/appointments')
def getappointments():
    # return jsonify(appointments)
    return jsonify({'appointments': appointments})


@app.route('/appointments/<string:appointment_name>')
def getappointment(appointment_name):
    appointmentsFound = [
        appointment for appointment in appointments if appointment['name'] == appointment_name.lower()]
    if (len(appointmentsFound) > 0):
        return jsonify({'appointment': appointmentsFound[0]})
    return jsonify({'message': 'appointment Not found'})

# Create Data Routes
@app.route('/appointments', methods=['POST'])
def addappointment():
    new_appointment = {
        'name': request.json['name'],
        'lastname': request.json['lastname'],
        'document': request.json['document'],
        'birthday': request.json['birthday'],
        'city': request.json['city'],
        'neighborhood': request.json['neighborhood'],
        'phone': request.json['phone'],
        
    }
    appointments.append(new_appointment)
    return jsonify({'appointments': appointments})

# Update Data 
@app.route('/appointments/<string:appointment_name>', methods=['PUT'])
def editappointment(appointment_name):
    appointmentsFound = [appointment for appointment in appointments if appointment['name'] == appointment_name]
    if (len(appointmentsFound) > 0):
        appointmentsFound[0]['name'] = request.json['name']
        appointmentsFound[0]['lastname'] = request.json['lastname']
        appointmentsFound[0]['document'] = request.json['document']
        appointmentsFound[0]['birthday'] = request.json['birthday']
        appointmentsFound[0]['city'] = request.json['city']
        appointmentsFound[0]['neighborhood'] = request.json['neighborhood']
        appointmentsFound[0]['phone'] = request.json['phone']

        return jsonify({
            'message': 'appointment Updated',
            'product': appointmentsFound[0]
        })
    return jsonify({'message': 'appointment Not found'})

# DELETE Data                                   
@app.route('/appointments/<string:appointment_name>', methods=['DELETE'])
def deleteappointment(appointment_name):
    appointmentsFound = [appointment for appointment  in appointments if appointment['name'] == appointment_name]
    if len(appointmentsFound) > 0:
        appointments.remove(appointmentsFound[0])
        return jsonify({
            'message': 'appointment Deleted',
            'appointments':appointments
        })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
