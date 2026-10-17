#!/usr/bin/env ruby
# frozen_string_literal: true

require "yaml"

path = ARGV.fetch(0, "skills/academic-claim-calibration/SKILL.md")
text = File.read(path, encoding: "UTF-8")
match = /\A---\n(.*?)\n---(?:\n|\z)/m.match(text)
abort("#{path}: YAML frontmatter is missing") unless match

data = YAML.safe_load(match[1], permitted_classes: [], aliases: false)
abort("#{path}: frontmatter must be a mapping") unless data.is_a?(Hash)

name = data["name"]
description = data["description"]
unless name.is_a?(String) && name.match?(/\A[a-z0-9]+(?:-[a-z0-9]+)*\z/)
  abort("#{path}: name must use lowercase letters, numbers, and hyphens")
end

if !description.is_a?(String) || description.strip.length < 20
  abort("#{path}: description is missing or too short")
end

puts "validated YAML frontmatter: #{name}"
