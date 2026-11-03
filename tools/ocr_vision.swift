// On-device OCR (Apple Vision) used by tools/fs_auditor.py to read an auditor's signature that a PDF holds only as an
// image. Build on macOS: swiftc -O tools/ocr_vision.swift -o tools/ocr   (or set CCH_OCR to the binary's path)
// usage: ocr <image.png>  -> recognised text lines, top to bottom
import Foundation
import Vision
import AppKit
let path = CommandLine.arguments[1]
guard let img = NSImage(contentsOfFile: path), let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { exit(1) }
let req = VNRecognizeTextRequest()
req.recognitionLevel = .accurate
req.usesLanguageCorrection = false
try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
for o in (req.results ?? []) { if let t = o.topCandidates(1).first { print(t.string) } }
