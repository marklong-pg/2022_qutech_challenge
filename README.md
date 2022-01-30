# QueueMeet
**A prototype conference call software utilizing quantum key distribution for telemedicine applications.**

<img width="586" alt="Screenshot 2022-01-30 at 19 42 44" src="https://user-images.githubusercontent.com/53221131/151696489-60ef17a0-62e3-49e9-b77b-a6eb7aed8075.png">

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

## Our Experience at IT iQuHACK 2022
Mark Long:
Tristan Austin:
Freya Shah:
Paridhi Jain: It was a very enriching experience for me, I am still a novice in quantum computing field and I learnt a lot from my fellow teammates. It was highly enjoyable and super cool to work with my teammates. It was interesting that we were all from different time zones and we were working together variedly. Looking forward to work with them again! :))
Hyun Lee: Amazing three days with great people. It was a bit hard to get teammates in gather town but after all, I met super cool teammates and learnt a lot from them. It was so fun to see our brainstorming finally flows in one direction. Experience of making something together with others which I can't make by myself gave me such a big energy to dive more into this quantum computing field. Thank you iQuHACK 2022 for this wonderful event!  
