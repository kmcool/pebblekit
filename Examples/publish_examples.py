#!/usr/bin/python

from sh import rm, git, cp, cd
import argparse


def upload_examples(version):
  try:
    rm("-rf", "pebble-sdk-examples")
  except:
    pass

  examples = ["data-logging-demo", "golf-demo", "pebblekit-js", "sports-demo", "todolist-demo", "watchapps", "watchfaces", "weather-demo"]

  git("clone", "git@github.com:pebble/pebble-sdk-examples.git")
  rm("-rf", "pebble-sdk-examples/*")
  cp("-r", examples, "pebble-sdk-examples")
  cp("README.md", "pebble-sdk-examples")
  cd("pebble-sdk-examples")
  git("add", "-u", ".")
  git("add", "-A", ".")
  git("commit", "-m", "Releasing Examples for version {}".format(version))

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Push sdk examples to github')
  parser.add_argument('version')

  args = parser.parse_args()

  upload_examples(args.version)
