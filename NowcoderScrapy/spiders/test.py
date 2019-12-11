import re
# selectors = ['//*[@id="priceblock_ourprice"]/text()',
#              '//*[@id="olp-sl-new.asin"]/span/span/text()',
#              '//*[@id="olp-new.asin"]/span/span/text()',
#              '//*[@id="priceblock_dealprice"]/text()',
#
#              '//*[@id="olp-upd-new-freeshipping"]/a/span/text()',
#              '//*[@id="olp-new"]/span/span/text()',
#              '//*[@id="olp-upd-new"]/a/span/text()',
#              '//*[@id="olp-upd-new-freeshipping-threshold"]/a/span/text()',
#              '//*[@id="olp-sl-new"]/span/span/text()',
#              '//*[@id="olp-sl-new-openbox"]/span[1]/span/text()', ]
# for i in range(0, len(selectors)):
#     print(selectors[i])

response = "655 236 134"
print(re.search("236 | 655", response).group())