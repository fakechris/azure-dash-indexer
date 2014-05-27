# Scrapy settings for azure_cmdlets project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'azure_cmdlets'

SPIDER_MODULES = ['azure_cmdlets.spiders']
NEWSPIDER_MODULE = 'azure_cmdlets.spiders'

ITEM_PIPELINES = [
    'azure_cmdlets.pipelines.AzureCmdletsPipeline',
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'azure_cmdlets (+http://www.yourdomain.com)'
