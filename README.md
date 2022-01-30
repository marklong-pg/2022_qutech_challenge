# QueueMeet

A prototype conference call software utilizing quantum key distribution for telemedicine applications.

The application can be seperated into four different subsections:
1. Quantum Key Distribution (QKD)
2. openCV Integration
3. User Interface
4. Native Socket Server
5. VQE Client Host Optimization

The purpose and implementation of each section will be outlined below.

## Quantum Key Distribution
Quantum key distribution is an interesting application of quantum computing and quantum communication. Using the fact that measurement of qubits causes them to collapse into specific states depending on what basis they are encoded in, allows agents to communicate encrypted keys that are impossible to eavesdrop on. Essentially, the agents using QKD would be able to detect, within a very small margin of error, if someone was listening to their messages.

This aspect of the application was developed using Qiskit and numpy. It followed the BB84 encryption technique. More specifically, it involved generateing random bit strings, encoding them into random bases, measuring them in random bases, comparing the encoded and measured bases, and then sharing a small sample of the bit strings to determine the presence of an eavesdropper. The final key, after discarding the sample, is completely private to a really high accuracy. This section of the code generates keys for each agent in the conference call.

## OpenCV Integration
OpenCV enables tracking and recognizing the QR codes from a user's camera. As medical data like the x-ray images we used as examples should be concerned with a high level of data security, the QR code is containing the file path of the wanted file in the hospital server, not the data itself. Combined with QKD, only the person who needs to see a particular x-ray image can reach the file in the hospital database with the right key and the other participants can not open the image file even if they capture the QR code in the conference call.    

## User Interface
The UI was coded using PySimpleGUI. It involves very simple image display features and utilitizes the QR code recognition from openCV. 

## Native Socket Server


## VQE Client Host Optimization
As the number of people between who the information is to be shared increases it becomes difficult to figure out the best possible and optimal way to set up quantum channels between them. This problem becomes similar to Travelling Salesman Problem which is an optimisation problem. As a prototype of what further could be done with this project we have solved this problem using Variational Quantum Eigensolver. Thus as the number of people and distances increase an optimal way to set up the quantum channels can be determined.


## Quick Tutorial

