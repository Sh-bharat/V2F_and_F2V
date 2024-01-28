# Vedio to Frame and Frame to Vedioimport cv2
import os

output_frames=[]
path=input("Enter Vedio Path : ")
if (os.path.exists(path)):
    vedio = cv2.VideoCapture(path)
    print("Found")
    success,image=vedio.read()
    height, width, layers = image.shape
    size = (width,height)
    fps = vedio.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps)

    while success:        
        success, image = vedio.read() 
#         image is an 3D Array of RGB image 
        
        
        
        
        
        image1=image
        output_frames.append(image1)        
        
    out = cv2.VideoWriter('Output.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, size) 
    for i in range(len(output_frames)):
        out.write(output_frames[i])
    out.release()
else:
    raise IOError("Error: File  not Found. ")
