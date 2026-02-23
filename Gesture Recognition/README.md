# Hand Gesture Recognition

Real-time hand gesture recognition using MediaPipe and OpenCV. Detects 11 gestures via webcam with temporal smoothing and a clean HUD overlay.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?style=flat-square)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10+-orange?style=flat-square)

---

## Gestures

| Gesture | Pattern (T I M R P) |
|---|---|
| Thumbs Up | 1 0 0 0 0 |
| Fist | 0 0 0 0 0 |
| Open Palm | 1 1 1 1 1 |
| Peace | 0 1 1 0 0 |
| Point | 0 1 0 0 0 |
| Pinky Up | 0 0 0 0 1 |
| Rock On | 0 1 0 0 1 |
| Gun | 1 1 0 0 0 |
| Three | 0 1 1 1 0 |
| Four | 0 1 1 1 1 |
| Three-Alt | 1 1 1 0 0 |

---

## Requirements

```
opencv-python
mediapipe
numpy
```

Install with:

```bash
pip install opencv-python mediapipe numpy
```

---

## Usage

```bash
python main.py
```

Press `Q` or `Esc` to quit.

---

## How It Works

- **Finger detection** — measures joint angles at each PIP joint to compute a curl score (0.0 = extended, 1.0 = curled). Fingers with a curl score below 0.4 are counted as extended.
- **Thumb detection** — uses the MCP joint angle and tip distance from the index finger base for reliable left/right hand handling.
- **Temporal smoothing** — gesture labels are smoothed over a 10-frame rolling window using majority vote, eliminating flicker on borderline frames.
- **UI** — frosted bottom panel with centered gesture name, per-finger indicator bar (T I M R P), and FPS counter. Hand skeleton uses custom drawing with gold fingertip highlights.

---

## Project Structure

```
├── main.py       # Entry point — all logic in one file
└── README.md
```

---

## License

MIT
