#!/usr/bin/env ruby
puts ARGV[0].scan(/\bfrom:\s*(.*?)\b\].+\bto:\s*(.*?)\b\].+\bflags:\s*(.*?)\b\]/).join(",")
