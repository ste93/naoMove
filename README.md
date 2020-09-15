# naoMove
Required packages:
- matplotlib
- deap
- numpy
- pyjarowinkler
- distance
- bcolors

made on python 2.7

The project is derived from project Sandro https://github.com/PinsonJonas/Project-2-sandro and allows the user to move the nao with some json files
The Json structure of each file is: 
  - For the kinect files:
    
    { "name": "filename",
    
      "datafile": [
        
        {"coord" : "1",
        
        "data" : [
          { 
          
            "jointname" : ""
          
              "coordinates" : [
              
              x,
              
              y,
              
              Z
            
            ]
          
          },
          
          ...
          
         ]
      
       }, 
        
       ...
     
     }
     
     
     Jointnames allowed are: 
         "HipCenter", "Spine", "ShoulderCenter", "Head", "ShoulderLeft", "ElbowLeft", "WristLeft", "HandLeft", "ShoulderRight", "ElbowRight", "WristRight", "HandRight", "HipLeft", "KneeLeft", "AnkleLeft", "FootLeft", "HipRight", "KneeRight", "AnkleRight", "FootRight"
