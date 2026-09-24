// ocr <image> : recognized text lines, top to bottom (Vision, accurate, en-US)
import Vision
import AppKit
let url = URL(fileURLWithPath: CommandLine.arguments[1])
guard let img = NSImage(contentsOf: url), let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { exit(1) }
let req = VNRecognizeTextRequest()
req.recognitionLevel = .accurate
req.usesLanguageCorrection = false
req.recognitionLanguages = ["en-US"]
try VNImageRequestHandler(cgImage: cg).perform([req])
for o in (req.results ?? []).sorted(by: { $0.boundingBox.minY > $1.boundingBox.minY }) {
    if let t = o.topCandidates(1).first?.string { print(t) }
}
