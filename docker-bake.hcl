group "default" {
  targets = ["plone", "zeoserver"]
}

target "plone" {
  name = "plone-alpine${replace(alpine_version, ".", "-")}"
  context = "./plone"
  matrix = {
    alpine_version = ["3.20", "3.21", "3.22"]
  }
  args = {
    ALPINE_VERSION = alpine_version
  }
  tags = [
    "docker.io/4teamwork/plone:4.3.20-alpine${alpine_version}",
    equal(alpine_version, "3.22") ? "docker.io/4teamwork/plone:4.3.20" : "",
  ]
  platforms = [
    "linux/amd64",
    "linux/arm64"
  ]
}

target "zeoserver" {
  name = "zeoserver-alpine${replace(alpine_version, ".", "-")}"
  context = "./zeoserver"
  matrix = {
    alpine_version = ["3.20", "3.21", "3.22"]
  }
  args = {
    ALPINE_VERSION = alpine_version
  }
  tags = [
    "docker.io/4teamwork/zeoserver:4.3.20-alpine${alpine_version}",
    equal(alpine_version, "3.22") ? "docker.io/4teamwork/zeoserver:4.3.20" : "",
  ]
  platforms = [
    "linux/amd64",
    "linux/arm64"
  ]
}
