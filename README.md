# vid10mb

A work-in-progress CLI (and future GUI) for crushing video files down so they fit comfortably under a target size — with 10 MB as the default cap. The long-term goal is to make trimming, transcoding, and compressing clips trivial for sharing on platforms with strict upload limits.

## Current Status
- ✅ Python package skeleton with an entry-point script (`vid10mb`).
- ✅ Basic CLI argument parsing for input path, optional output path, and target size.
- 🚧 Encoding pipeline still a stub — currently only echoes the requested operation.
- 🚧 No GUI yet.

## Why 10 MB?
Many chat tools, forums, and issue trackers cap attachments at 8–25 MB. Hitting a predictable 10 MB target keeps clips universally shareable without guesswork.

## Prerequisites
- Python 3.10+
- `ffmpeg` available on your PATH (compression pipeline will call into it)

## Installation (development mode)
```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .
```

## Quick Start
```bash
vid10mb my_clip.mov --max-mb 10
```
For now this prints the parameters it would use. Wiring up the actual `ffmpeg` command is the next major milestone.

## Roadmap
1. Implement file-size-aware bitrate targeting and invoke `ffmpeg` for transcoding.
2. Provide quality presets (e.g., fast/standard/high).
3. Auto-generate an output filename when `-o/--output` is omitted.
4. Surface progress and final file stats in the CLI.
5. Add end-to-end tests with sample media under `tests/`.
6. Explore a lightweight GUI wrapper for drag-and-drop conversions.

## Development Notes
- Keep sample media small and under version-control limits; use the `samples/` directory.
- Prefer asynchronous `ffmpeg` execution so a GUI can reuse the core pipeline.
- Ensure new features ship with tests once the clip-processing code lands.

## Contributing
Open issues and pull requests welcome. Start with the roadmap above or propose new ideas for making sub-10 MB sharing easier.
