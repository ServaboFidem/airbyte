#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


import sys

from destination_opensearch import DestinationOpensearch

if __name__ == "__main__":
    DestinationOpensearch().run(sys.argv[1:])
