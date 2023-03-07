import cv2

def main():
    try:
        #reading the video stream(file)
        cap = cv2.VideoCapture("demo-1.mp4")
        output = cv2.VideoWriter("demo-modified-1.avi", cv2.VideoWriter_fourcc(*'DIVX'), 30.0, (int(cap.get(3)),int(cap.get(4))))

        while(True):
            ret, frame = cap.read()
            if(ret):
                cv2.rectangle(frame, (0,0), (1920,50), (0, 255, 0), -1)
                output.write(frame)
                cv2.imshow("output", frame)
                if cv2.waitKey(1) & 0xFF == ord('s'):
                    break
            else:
                break

        cv2.destroyAllWindows()
        output.release()
        cap.release()
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
 