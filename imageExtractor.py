import cv2
import os


numberOfClips = 23
imageNumber = 317
nthImage = 60

# FIXME, adjusted to extract from one video
for clipNumber in range(numberOfClips, numberOfClips + 2):
    print(f"Images from Clip #{clipNumber}")
    clip = cv2.VideoCapture(f"C:\\Users\\isss1\\OneDrive\\Documents\\Wondershare\\Wondershare Filmora\\Output\\clip_{clipNumber}.mp4")

    try:
        if not os.path.exists('images'):
            os.makedirs('images')
    except OSError:
        print('Error creating the directory to store images.')

    currentFrame = 0
    
    while(True): 
        
        # reading from frame 
        ret, frame = clip.read() 
    
        if ret: 
            # if video is still left continue creating images 
            # Only obtaining the nth image of each frame for image detection, to not have too many of the same images

            if currentFrame % nthImage == 0:
                imageNumber += 1
                name = './images/frame' + str(imageNumber) + '.jpg'
                print ('Creating...' + name) 
        
                # writing the extracted images 
                cv2.imwrite(name, frame) 
    
            # increasing counter so that it will 
            # show how many frames are created 
            currentFrame += 1
        else: 
            break
    
    # Release all space and windows once done 
    clip.release() 
    cv2.destroyAllWindows() 