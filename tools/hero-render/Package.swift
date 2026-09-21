// swift-tools-version: 6.2
import PackageDescription
let package = Package(
    name: "hero-render",
    platforms: [.macOS(.v15)],
    dependencies: [.package(url: "https://github.com/redtear1115/mars-dawn-kit.git", exact: "0.5.1")],
    targets: [.executableTarget(name: "hero-render", dependencies: [.product(name: "MarsDawnKit", package: "mars-dawn-kit")])]
)
