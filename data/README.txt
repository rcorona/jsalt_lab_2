Papers:
1) Nitin Jindal, Bing Liu and Ee Peng Lim. Finding Unusual Review Patterns Using Unexpected Rules. Proceedings of 19th ACM International Conference on Information and Knowledge Management, CIKM'10, Toronto, Canada. October 2010. (short paper)
2) Ee Peng Lim, Viet An Nguyen, Nitin Jindal, Bing Liu and Hady Lauw. Detecting Product Review Spammers Using Rating Behavior. To appear in 19th ACM  Proceedings of 19th ACM International Conference on Information and Knowledge Management, CIKM'10, Toronto, Canada. October 2010.
3) Nitin Jindal and Bing Liu. Opinion Spam and Analysis. Proceedings of 1st ACM International Conference on Web Search and Data Mining, WSDM '08. Stanford University, California 2008.
4) Nitin Jindal and Bing Liu. Review Spam Detection. Proceedings of 16th International World Wide Web conference, WWW '07. Banff, Alberta, Canada 2007. (poster paper).
5) Arjun Mukherjee, Bing Liu, Junhui Wang, Natalie Glance, and Nitin Jindal. Detecting Group Review Spam. WWW'2011 (poster).
6) Arjun Mukherjee, Bing Liu, and Natalie Glance. Spotting Fake Reviewer Groups in Consumer Reviews. WWW'2012.

1) File reviewsNew.rar
Each row is TAB separated list of following
<member id> \t <product id> \t <date> \t <number of helpful feedbacks> \t <number of feedbacks> \t <rating> \t <title> \t <body>

2) File productinfo.rar
This file contains only the following information on products. We still have the product home pages that we crawled. So, I can run my extraction code again to get additional
information we want like Book Publisher, etc.
BREAK-REVIEWED //Or just the word BREAK for producst which dont have reviews
<product id> \t <product name> \t <product type> \t <Brand> \t <sales price> \t <list price> \t \t <short product description>
Product Category Path 1
Product Category Path 2
...

3) File amazon-member-shortSummary.txt
MEMBER INFO
<member id> <member name> <#reviews>
<In my own words>

4) File amazon-memberinfo-locations.txt
Each row is TAB separated list of following
<username> <member rank> <birthday> <location> <name> <memberid> <state>

5) File productInfoXML-mProducts.txt
This file is info on products from manufactured products category downloaded directly using amazon web services
BREAK-REVIEWED
<ProductID> \t <Sales Rank> \t <Brand> \t <Sales Price> \t <Title>
<Category->Value> \t <Category->Value> \t <Category->Value> ....

6) File productInfoXML-AudioCDs.txt
This file is info on products from Audio CDs category downloaded directly using amazon web services
BREAK-REVIEWED
<ProductID> \t <Sales Rank> \t <Label> \t <Sales Price>
<Category->Value> \t <Category->Value> \t <Category->Value> ....

7) File BooksInfo.txt
Extra information on books. The first row contains the column names. The remaining rows are data records. The columns are
RowID, ProductID, Publisher, ReleaseDate, ProductDimensions, ShippingWeight, Language, NumPages, Type, Edition, FullDesc
