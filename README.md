# QueueMeet

A prototype conference call software utilizing quantum key distribution for telemedicine applications.

The application can be seperated into four different subsections:
1. Quantum Key Distribution (QKD)
2. openCV Integration
3. User Interface
4. Django Server

The purpose and implementation of each section will be outlined below.

## Quantum Key Distribution
Quantum key distribution is an interesting application of quantum computing and quantum communication. Using the fact that measurement of qubits causes them to collapse into specific states depending on what basis they are encoded in, allows agents to communicate encrypted keys that are impossible to eavesdrop on. Essentially, the agents using QKD would be able to detect, within a very small margin of error, if someone was listening to their messages.

This aspect of the application was developed using Qiskit and numpy. It followed the BB84 encryption technique. More specifically, it involved generateing random bit strings, encoding them into random bases, measuring them in random bases, comparing the encoded and measured bases, and then sharing a small sample of the bit strings to determine the presence of an eavesdropper. The final key, after discarding the sample, is completely private to a really high accuracy. This section of the code generates keys for each agent in the conference call.

## OpenCV Integration

## User Interface
The UI was coded using PySimpleGUI. It involves very simple image display features and utilitizes the QR code recognition from openCV. 

## Django Server

## Quick Tutorial

