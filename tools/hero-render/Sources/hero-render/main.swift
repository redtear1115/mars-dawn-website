import Foundation
import MarsDawnKit

// Default: reads Markdown on stdin, writes MarsDawnKit's preview HTML on stdout.
// `--theme-css`: writes the kit's generated theme stylesheet (PreviewTheme.stylesheet)
// instead, so the website can vendor it without duplicating the palette by hand.
if CommandLine.arguments.dropFirst().first == "--theme-css" {
    print(PreviewTheme.stylesheet, terminator: "")
} else {
    let data = FileHandle.standardInput.readDataToEndOfFile()
    print(MarkdownRenderer.render(String(decoding: data, as: UTF8.self)), terminator: "")
}
