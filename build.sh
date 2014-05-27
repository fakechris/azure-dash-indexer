#!/bin/sh

#scrapy crawl azure
mkdir -p "/Users/chris/Library/Application Support/Dash/DocSets/AzureCmdlets.docset/Contents/Resources/Documents/"

cp -r download/* "/Users/chris/Library/Application Support/Dash/DocSets/AzureCmdlets.docset/Contents/Resources/Documents/"

cp Info.plist "/Users/chris/Library/Application Support/Dash/DocSets/AzureCmdlets.docset/Contents"

cp azure.db "/Users/chris/Library/Application Support/Dash/DocSets/AzureCmdlets.docset/Contents/Resources/docSet.dsidx"
