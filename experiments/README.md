# Tracker experiments

Small webcam scripts used to compare landmark trackers before choosing MediaPipe Face Mesh.
Press `w` to save a screenshot, `q` to quit.

| Script | Tracker | Landmarks |
|---|---|---|
| `mediapipe_facemesh.py` | MediaPipe Face Mesh | 468 (3D) |
| `dlib_68_landmarks.py` | dlib ERT shape predictor | 68 (2D) |

`dlib_68_landmarks.py` needs `shape_predictor_68_face_landmarks.dat` from
[dlib.net](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) in the working directory.
Check the model's license terms before any commercial use.
