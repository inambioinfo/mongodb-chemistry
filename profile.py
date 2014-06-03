#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Benchmark chemical similarity searches in MongoDB and PostgreSQL."""

import datetime
import random
import time

import numpy as np
import pymongo
import psycopg2


def choose_random():
    """Choose 1000 random molecules from the database."""
    db = pymongo.MongoClient().chem
    # Get all CHEMBL IDs
    db.molecules.ensure_index('chembl_id')
    chembl_ids = [m['chembl_id'] for m in db.molecules.find().sort('chembl_id')]
    print len(chembl_ids)
    random.seed(201405291515)
    rands = random.sample(chembl_ids, 1000)
    print rands

# These 1000 CHEMBL IDs were chosen using the above choose_random() function
chembl_ids = [u'CHEMBL129715', u'CHEMBL1906145', u'CHEMBL551275', u'CHEMBL2386972', u'CHEMBL1899063', u'CHEMBL1618426', u'CHEMBL1990584', u'CHEMBL229304', u'CHEMBL1322309', u'CHEMBL1560934', u'CHEMBL1587570', u'CHEMBL1730123', u'CHEMBL2331979', u'CHEMBL132497', u'CHEMBL1383522', u'CHEMBL1520610', u'CHEMBL2392139', u'CHEMBL550020', u'CHEMBL2437213', u'CHEMBL535881', u'CHEMBL1536347', u'CHEMBL1565839', u'CHEMBL1326035', u'CHEMBL2074932', u'CHEMBL1324964', u'CHEMBL378585', u'CHEMBL1401247', u'CHEMBL84180', u'CHEMBL1999636', u'CHEMBL92142', u'CHEMBL1469945', u'CHEMBL1543926', u'CHEMBL2164555', u'CHEMBL2221099', u'CHEMBL206307', u'CHEMBL573195', u'CHEMBL2152465', u'CHEMBL2372234', u'CHEMBL517915', u'CHEMBL2409818', u'CHEMBL1900656', u'CHEMBL1927332', u'CHEMBL16430', u'CHEMBL1503235', u'CHEMBL1412987', u'CHEMBL1587760', u'CHEMBL1272105', u'CHEMBL476894', u'CHEMBL433932', u'CHEMBL2414401', u'CHEMBL1582102', u'CHEMBL231349', u'CHEMBL318981', u'CHEMBL1406092', u'CHEMBL212272', u'CHEMBL1972182', u'CHEMBL1801946', u'CHEMBL1869168', u'CHEMBL1327165', u'CHEMBL1428200', u'CHEMBL1873599', u'CHEMBL575329', u'CHEMBL1977041', u'CHEMBL1353028', u'CHEMBL366251', u'CHEMBL186999', u'CHEMBL1209570', u'CHEMBL278704', u'CHEMBL2058240', u'CHEMBL413668', u'CHEMBL2206277', u'CHEMBL1353742', u'CHEMBL1784567', u'CHEMBL1312558', u'CHEMBL448229', u'CHEMBL1998891', u'CHEMBL55831', u'CHEMBL9269', u'CHEMBL582019', u'CHEMBL266969', u'CHEMBL326900', u'CHEMBL1289081', u'CHEMBL399527', u'CHEMBL1394384', u'CHEMBL440022', u'CHEMBL1504443', u'CHEMBL1437627', u'CHEMBL2324150', u'CHEMBL1702511', u'CHEMBL2041564', u'CHEMBL1730602', u'CHEMBL21329', u'CHEMBL2403780', u'CHEMBL478387', u'CHEMBL1401843', u'CHEMBL1716322', u'CHEMBL2094196', u'CHEMBL2008945', u'CHEMBL2425030', u'CHEMBL1402386', u'CHEMBL2371787', u'CHEMBL1276021', u'CHEMBL1511901', u'CHEMBL2059484', u'CHEMBL2220674', u'CHEMBL1609446', u'CHEMBL1713327', u'CHEMBL1477299', u'CHEMBL1542283', u'CHEMBL1387526', u'CHEMBL1796512', u'CHEMBL1890721', u'CHEMBL1363016', u'CHEMBL21779', u'CHEMBL226732', u'CHEMBL2365627', u'CHEMBL2036635', u'CHEMBL1596678', u'CHEMBL1185098', u'CHEMBL461384', u'CHEMBL399042', u'CHEMBL1367612', u'CHEMBL489806', u'CHEMBL2140716', u'CHEMBL610860', u'CHEMBL271896', u'CHEMBL595947', u'CHEMBL112658', u'CHEMBL1643671', u'CHEMBL522298', u'CHEMBL1170088', u'CHEMBL2177346', u'CHEMBL307771', u'CHEMBL1194657', u'CHEMBL255569', u'CHEMBL63561', u'CHEMBL194474', u'CHEMBL472091', u'CHEMBL1089224', u'CHEMBL493767', u'CHEMBL1382832', u'CHEMBL518969', u'CHEMBL1906245', u'CHEMBL2068691', u'CHEMBL1567672', u'CHEMBL2338280', u'CHEMBL1377272', u'CHEMBL423018', u'CHEMBL594911', u'CHEMBL494811', u'CHEMBL581438', u'CHEMBL278733', u'CHEMBL541628', u'CHEMBL304262', u'CHEMBL1324956', u'CHEMBL2138939', u'CHEMBL1338909', u'CHEMBL1189205', u'CHEMBL104900', u'CHEMBL1591941', u'CHEMBL560437', u'CHEMBL1078985', u'CHEMBL1834118', u'CHEMBL1331290', u'CHEMBL453102', u'CHEMBL1765498', u'CHEMBL2408684', u'CHEMBL607515', u'CHEMBL1348130', u'CHEMBL2112129', u'CHEMBL1552602', u'CHEMBL526918', u'CHEMBL1474979', u'CHEMBL2205652', u'CHEMBL10208', u'CHEMBL1836258', u'CHEMBL2112178', u'CHEMBL1448255', u'CHEMBL1735459', u'CHEMBL1722581', u'CHEMBL328709', u'CHEMBL169622', u'CHEMBL511834', u'CHEMBL1570599', u'CHEMBL30505', u'CHEMBL188455', u'CHEMBL2205646', u'CHEMBL1411233', u'CHEMBL2355525', u'CHEMBL482785', u'CHEMBL129654', u'CHEMBL376945', u'CHEMBL1253398', u'CHEMBL441668', u'CHEMBL35291', u'CHEMBL1197945', u'CHEMBL7679', u'CHEMBL190800', u'CHEMBL491519', u'CHEMBL512977', u'CHEMBL121302', u'CHEMBL611811', u'CHEMBL1861204', u'CHEMBL15447', u'CHEMBL1703375', u'CHEMBL1082332', u'CHEMBL1406003', u'CHEMBL1607231', u'CHEMBL1414407', u'CHEMBL1254898', u'CHEMBL1835265', u'CHEMBL444445', u'CHEMBL575506', u'CHEMBL386308', u'CHEMBL1603754', u'CHEMBL1160378', u'CHEMBL1642728', u'CHEMBL457409', u'CHEMBL1813826', u'CHEMBL1190511', u'CHEMBL1338755', u'CHEMBL1451595', u'CHEMBL1982213', u'CHEMBL2436066', u'CHEMBL2435054', u'CHEMBL2059214', u'CHEMBL1512410', u'CHEMBL1880793', u'CHEMBL1446010', u'CHEMBL1564662', u'CHEMBL1608779', u'CHEMBL358147', u'CHEMBL189875', u'CHEMBL1425157', u'CHEMBL308024', u'CHEMBL193158', u'CHEMBL291096', u'CHEMBL456274', u'CHEMBL1349655', u'CHEMBL1714604', u'CHEMBL1491783', u'CHEMBL1508168', u'CHEMBL1360559', u'CHEMBL2348097', u'CHEMBL2374148', u'CHEMBL194913', u'CHEMBL2206686', u'CHEMBL2357782', u'CHEMBL1798058', u'CHEMBL576329', u'CHEMBL2372454', u'CHEMBL1698057', u'CHEMBL288441', u'CHEMBL186511', u'CHEMBL1465893', u'CHEMBL1408312', u'CHEMBL1974146', u'CHEMBL1199191', u'CHEMBL96936', u'CHEMBL1822531', u'CHEMBL2087656', u'CHEMBL2357746', u'CHEMBL2312015', u'CHEMBL547683', u'CHEMBL8663', u'CHEMBL319408', u'CHEMBL32557', u'CHEMBL1879947', u'CHEMBL326102', u'CHEMBL2436769', u'CHEMBL1966442', u'CHEMBL1411942', u'CHEMBL2436346', u'CHEMBL1076121', u'CHEMBL1865590', u'CHEMBL359291', u'CHEMBL80535', u'CHEMBL38085', u'CHEMBL295325', u'CHEMBL84454', u'CHEMBL2030285', u'CHEMBL474842', u'CHEMBL1985028', u'CHEMBL27036', u'CHEMBL1188727', u'CHEMBL2134519', u'CHEMBL374598', u'CHEMBL587458', u'CHEMBL2347263', u'CHEMBL574435', u'CHEMBL2386452', u'CHEMBL508557', u'CHEMBL1527334', u'CHEMBL1563990', u'CHEMBL340069', u'CHEMBL1427120', u'CHEMBL1436954', u'CHEMBL2011356', u'CHEMBL1983597', u'CHEMBL1618299', u'CHEMBL1479549', u'CHEMBL1388682', u'CHEMBL462505', u'CHEMBL1241587', u'CHEMBL1510771', u'CHEMBL1366299', u'CHEMBL596328', u'CHEMBL587886', u'CHEMBL360334', u'CHEMBL431421', u'CHEMBL2142833', u'CHEMBL433045', u'CHEMBL1593602', u'CHEMBL199027', u'CHEMBL61590', u'CHEMBL17007', u'CHEMBL1607308', u'CHEMBL62463', u'CHEMBL1326385', u'CHEMBL1199439', u'CHEMBL602341', u'CHEMBL93926', u'CHEMBL1300898', u'CHEMBL1950321', u'CHEMBL245707', u'CHEMBL1577312', u'CHEMBL40209', u'CHEMBL1794944', u'CHEMBL1595214', u'CHEMBL2362373', u'CHEMBL68216', u'CHEMBL1191069', u'CHEMBL236842', u'CHEMBL1457823', u'CHEMBL1940993', u'CHEMBL1884884', u'CHEMBL1382957', u'CHEMBL442612', u'CHEMBL1361528', u'CHEMBL1601982', u'CHEMBL89999', u'CHEMBL1950625', u'CHEMBL1621139', u'CHEMBL208983', u'CHEMBL2138324', u'CHEMBL1797862', u'CHEMBL266279', u'CHEMBL1313644', u'CHEMBL1902331', u'CHEMBL2069146', u'CHEMBL286683', u'CHEMBL1329092', u'CHEMBL560287', u'CHEMBL251307', u'CHEMBL577783', u'CHEMBL494929', u'CHEMBL199711', u'CHEMBL1836874', u'CHEMBL27761', u'CHEMBL519874', u'CHEMBL87568', u'CHEMBL1897767', u'CHEMBL422679', u'CHEMBL2140728', u'CHEMBL1480013', u'CHEMBL1354676', u'CHEMBL1688923', u'CHEMBL612068', u'CHEMBL1481450', u'CHEMBL358287', u'CHEMBL513806', u'CHEMBL2430556', u'CHEMBL252912', u'CHEMBL1602857', u'CHEMBL1900571', u'CHEMBL2348567', u'CHEMBL1317737', u'CHEMBL1762725', u'CHEMBL1524039', u'CHEMBL2165629', u'CHEMBL1672633', u'CHEMBL2338482', u'CHEMBL275194', u'CHEMBL1884816', u'CHEMBL1312779', u'CHEMBL469014', u'CHEMBL299878', u'CHEMBL1612568', u'CHEMBL2151063', u'CHEMBL438427', u'CHEMBL1569109', u'CHEMBL2314218', u'CHEMBL431742', u'CHEMBL1333574', u'CHEMBL332871', u'CHEMBL199467', u'CHEMBL318349', u'CHEMBL1524125', u'CHEMBL1630053', u'CHEMBL2440761', u'CHEMBL274531', u'CHEMBL1164191', u'CHEMBL1458652', u'CHEMBL1198076', u'CHEMBL144817', u'CHEMBL542058', u'CHEMBL425764', u'CHEMBL1323815', u'CHEMBL1429924', u'CHEMBL1555307', u'CHEMBL1448426', u'CHEMBL2397428', u'CHEMBL374620', u'CHEMBL1407273', u'CHEMBL1335965', u'CHEMBL1499504', u'CHEMBL1462544', u'CHEMBL203721', u'CHEMBL1613075', u'CHEMBL401987', u'CHEMBL2220793', u'CHEMBL1923709', u'CHEMBL384907', u'CHEMBL1708598', u'CHEMBL420561', u'CHEMBL1739561', u'CHEMBL1814458', u'CHEMBL1484014', u'CHEMBL71786', u'CHEMBL2018644', u'CHEMBL1729644', u'CHEMBL1431051', u'CHEMBL1668264', u'CHEMBL1866160', u'CHEMBL1626991', u'CHEMBL1253202', u'CHEMBL1619646', u'CHEMBL574233', u'CHEMBL1967525', u'CHEMBL1582337', u'CHEMBL225535', u'CHEMBL3039241', u'CHEMBL1739334', u'CHEMBL1871615', u'CHEMBL2336182', u'CHEMBL1416481', u'CHEMBL243061', u'CHEMBL212054', u'CHEMBL1718604', u'CHEMBL1197732', u'CHEMBL1411930', u'CHEMBL444483', u'CHEMBL368883', u'CHEMBL486397', u'CHEMBL622', u'CHEMBL37945', u'CHEMBL2074684', u'CHEMBL1426106', u'CHEMBL175384', u'CHEMBL187634', u'CHEMBL513515', u'CHEMBL2414802', u'CHEMBL1672287', u'CHEMBL188167', u'CHEMBL1322888', u'CHEMBL1316232', u'CHEMBL2067948', u'CHEMBL15872', u'CHEMBL1882328', u'CHEMBL104486', u'CHEMBL1325183', u'CHEMBL1308505', u'CHEMBL31300', u'CHEMBL587518', u'CHEMBL1586705', u'CHEMBL2180158', u'CHEMBL1390484', u'CHEMBL62098', u'CHEMBL2336380', u'CHEMBL1497219', u'CHEMBL1819124', u'CHEMBL1511571', u'CHEMBL8715', u'CHEMBL1390307', u'CHEMBL547758', u'CHEMBL565411', u'CHEMBL112020', u'CHEMBL447379', u'CHEMBL1518979', u'CHEMBL1969713', u'CHEMBL256906', u'CHEMBL40370', u'CHEMBL2336092', u'CHEMBL1200932', u'CHEMBL1984614', u'CHEMBL14598', u'CHEMBL2178533', u'CHEMBL555598', u'CHEMBL1359455', u'CHEMBL2322264', u'CHEMBL368173', u'CHEMBL345110', u'CHEMBL1178553', u'CHEMBL2303760', u'CHEMBL249401', u'CHEMBL1783516', u'CHEMBL1605112', u'CHEMBL2023090', u'CHEMBL262849', u'CHEMBL1780216', u'CHEMBL207728', u'CHEMBL300701', u'CHEMBL63742', u'CHEMBL562666', u'CHEMBL1484715', u'CHEMBL1443572', u'CHEMBL2336450', u'CHEMBL1171279', u'CHEMBL46063', u'CHEMBL1432616', u'CHEMBL185620', u'CHEMBL1895211', u'CHEMBL1357302', u'CHEMBL358993', u'CHEMBL561262', u'CHEMBL57762', u'CHEMBL1420760', u'CHEMBL38480', u'CHEMBL220413', u'CHEMBL319625', u'CHEMBL1203972', u'CHEMBL1708831', u'CHEMBL1556917', u'CHEMBL87250', u'CHEMBL156187', u'CHEMBL205146', u'CHEMBL1485483', u'CHEMBL167287', u'CHEMBL1457210', u'CHEMBL154186', u'CHEMBL186783', u'CHEMBL205050', u'CHEMBL1535887', u'CHEMBL2022183', u'CHEMBL416955', u'CHEMBL1982468', u'CHEMBL1406635', u'CHEMBL1555848', u'CHEMBL2206395', u'CHEMBL60982', u'CHEMBL1162202', u'CHEMBL193744', u'CHEMBL338393', u'CHEMBL2017579', u'CHEMBL1491853', u'CHEMBL1683485', u'CHEMBL1604806', u'CHEMBL1711913', u'CHEMBL2087124', u'CHEMBL268232', u'CHEMBL1929524', u'CHEMBL1723762', u'CHEMBL319423', u'CHEMBL1704814', u'CHEMBL201122', u'CHEMBL54892', u'CHEMBL278776', u'CHEMBL1214621', u'CHEMBL37915', u'CHEMBL2113064', u'CHEMBL1091570', u'CHEMBL27928', u'CHEMBL419582', u'CHEMBL1645552', u'CHEMBL2089061', u'CHEMBL1726452', u'CHEMBL1834111', u'CHEMBL117226', u'CHEMBL1711565', u'CHEMBL532081', u'CHEMBL369492', u'CHEMBL1801232', u'CHEMBL1462135', u'CHEMBL349625', u'CHEMBL1438940', u'CHEMBL1869098', u'CHEMBL1939711', u'CHEMBL1365997', u'CHEMBL1379158', u'CHEMBL1442030', u'CHEMBL321020', u'CHEMBL2323488', u'CHEMBL47428', u'CHEMBL1863870', u'CHEMBL1078202', u'CHEMBL1214358', u'CHEMBL1450503', u'CHEMBL1172320', u'CHEMBL2312125', u'CHEMBL589298', u'CHEMBL205869', u'CHEMBL1271127', u'CHEMBL2139189', u'CHEMBL1789294', u'CHEMBL2437208', u'CHEMBL190334', u'CHEMBL79666', u'CHEMBL95611', u'CHEMBL280091', u'CHEMBL558986', u'CHEMBL2179254', u'CHEMBL183327', u'CHEMBL1426740', u'CHEMBL1965809', u'CHEMBL2001333', u'CHEMBL1579455', u'CHEMBL494468', u'CHEMBL415161', u'CHEMBL70849', u'CHEMBL597179', u'CHEMBL67226', u'CHEMBL358969', u'CHEMBL337186', u'CHEMBL1288645', u'CHEMBL592273', u'CHEMBL389134', u'CHEMBL525876', u'CHEMBL525558', u'CHEMBL40628', u'CHEMBL181721', u'CHEMBL1741614', u'CHEMBL1720107', u'CHEMBL231651', u'CHEMBL1766623', u'CHEMBL1522682', u'CHEMBL1255707', u'CHEMBL182752', u'CHEMBL579010', u'CHEMBL1545141', u'CHEMBL1378234', u'CHEMBL364856', u'CHEMBL1388077', u'CHEMBL385586', u'CHEMBL1288608', u'CHEMBL41710', u'CHEMBL1594873', u'CHEMBL559050', u'CHEMBL1080287', u'CHEMBL273339', u'CHEMBL155915', u'CHEMBL1928628', u'CHEMBL2028261', u'CHEMBL605790', u'CHEMBL257012', u'CHEMBL76618', u'CHEMBL93437', u'CHEMBL1353041', u'CHEMBL1876542', u'CHEMBL1163558', u'CHEMBL1512860', u'CHEMBL33102', u'CHEMBL1531043', u'CHEMBL1877477', u'CHEMBL348018', u'CHEMBL15063', u'CHEMBL232875', u'CHEMBL427835', u'CHEMBL1808535', u'CHEMBL336205', u'CHEMBL1834578', u'CHEMBL2159989', u'CHEMBL508471', u'CHEMBL1504267', u'CHEMBL321788', u'CHEMBL1762319', u'CHEMBL1232443', u'CHEMBL1568712', u'CHEMBL571556', u'CHEMBL405618', u'CHEMBL1516344', u'CHEMBL1830513', u'CHEMBL1573234', u'CHEMBL1651139', u'CHEMBL2136851', u'CHEMBL1609853', u'CHEMBL117057', u'CHEMBL1822686', u'CHEMBL492559', u'CHEMBL1605384', u'CHEMBL1884939', u'CHEMBL1736196', u'CHEMBL347725', u'CHEMBL564523', u'CHEMBL1791191', u'CHEMBL326154', u'CHEMBL1608396', u'CHEMBL315958', u'CHEMBL41865', u'CHEMBL102918', u'CHEMBL1917123', u'CHEMBL518473', u'CHEMBL18805', u'CHEMBL1495916', u'CHEMBL1417774', u'CHEMBL376899', u'CHEMBL2448395', u'CHEMBL2078981', u'CHEMBL1417224', u'CHEMBL576294', u'CHEMBL1807131', u'CHEMBL2208422', u'CHEMBL1506316', u'CHEMBL1483560', u'CHEMBL1454853', u'CHEMBL316055', u'CHEMBL171451', u'CHEMBL406312', u'CHEMBL1583806', u'CHEMBL1886020', u'CHEMBL2042270', u'CHEMBL190451', u'CHEMBL1592019', u'CHEMBL276515', u'CHEMBL134060', u'CHEMBL1223947', u'CHEMBL311665', u'CHEMBL539919', u'CHEMBL1592498', u'CHEMBL520713', u'CHEMBL2316122', u'CHEMBL373995', u'CHEMBL1419867', u'CHEMBL308558', u'CHEMBL1560960', u'CHEMBL475249', u'CHEMBL328555', u'CHEMBL1728493', u'CHEMBL448867', u'CHEMBL1976873', u'CHEMBL2069797', u'CHEMBL547908', u'CHEMBL1860811', u'CHEMBL70796', u'CHEMBL288193', u'CHEMBL2153147', u'CHEMBL1968036', u'CHEMBL578341', u'CHEMBL2107777', u'CHEMBL549950', u'CHEMBL49867', u'CHEMBL2007104', u'CHEMBL367347', u'CHEMBL179999', u'CHEMBL1946767', u'CHEMBL60641', u'CHEMBL1471020', u'CHEMBL60154', u'CHEMBL209263', u'CHEMBL1998116', u'CHEMBL141971', u'CHEMBL1684232', u'CHEMBL1411120', u'CHEMBL1403173', u'CHEMBL1683794', u'CHEMBL58132', u'CHEMBL1379910', u'CHEMBL383538', u'CHEMBL549719', u'CHEMBL1904224', u'CHEMBL1384700', u'CHEMBL2430026', u'CHEMBL1487337', u'CHEMBL1192196', u'CHEMBL420209', u'CHEMBL1335420', u'CHEMBL1346216', u'CHEMBL33654', u'CHEMBL598956', u'CHEMBL1530483', u'CHEMBL1408310', u'CHEMBL2131452', u'CHEMBL180146', u'CHEMBL1956293', u'CHEMBL1994029', u'CHEMBL433157', u'CHEMBL1322901', u'CHEMBL25948', u'CHEMBL240746', u'CHEMBL1487664', u'CHEMBL269867', u'CHEMBL1933158', u'CHEMBL1923806', u'CHEMBL321363', u'CHEMBL2003460', u'CHEMBL146267', u'CHEMBL454589', u'CHEMBL2431930', u'CHEMBL564441', u'CHEMBL2011420', u'CHEMBL1161417', u'CHEMBL39604', u'CHEMBL455550', u'CHEMBL2370031', u'CHEMBL1712577', u'CHEMBL224704', u'CHEMBL336768', u'CHEMBL496288', u'CHEMBL63932', u'CHEMBL107096', u'CHEMBL66748', u'CHEMBL215418', u'CHEMBL219791', u'CHEMBL1421619', u'CHEMBL3040734', u'CHEMBL409532', u'CHEMBL512208', u'CHEMBL1529612', u'CHEMBL1332356', u'CHEMBL1523577', u'CHEMBL1394999', u'CHEMBL1973429', u'CHEMBL2375134', u'CHEMBL1994202', u'CHEMBL274893', u'CHEMBL1543036', u'CHEMBL1480008', u'CHEMBL1524959', u'CHEMBL231005', u'CHEMBL351838', u'CHEMBL142253', u'CHEMBL1529997', u'CHEMBL370813', u'CHEMBL1935506', u'CHEMBL36889', u'CHEMBL1548349', u'CHEMBL1643906', u'CHEMBL2028574', u'CHEMBL1987598', u'CHEMBL1649939', u'CHEMBL101842', u'CHEMBL1526047', u'CHEMBL1530562', u'CHEMBL503987', u'CHEMBL2326103', u'CHEMBL144921', u'CHEMBL320803', u'CHEMBL1391439', u'CHEMBL516236', u'CHEMBL274142', u'CHEMBL252501', u'CHEMBL152146', u'CHEMBL2030277', u'CHEMBL2367637', u'CHEMBL453090', u'CHEMBL169934', u'CHEMBL1861923', u'CHEMBL481407', u'CHEMBL2008980', u'CHEMBL1987240', u'CHEMBL375357', u'CHEMBL1882218', u'CHEMBL2370022', u'CHEMBL205628', u'CHEMBL228111', u'CHEMBL1472261', u'CHEMBL1796817', u'CHEMBL2152165', u'CHEMBL1091355', u'CHEMBL2010893', u'CHEMBL1462316', u'CHEMBL1192935', u'CHEMBL33530', u'CHEMBL1644687', u'CHEMBL96264', u'CHEMBL1375898', u'CHEMBL1477640', u'CHEMBL304702', u'CHEMBL170283', u'CHEMBL1472407', u'CHEMBL1896783', u'CHEMBL1557625', u'CHEMBL1455569', u'CHEMBL478072', u'CHEMBL271265', u'CHEMBL1473813', u'CHEMBL1540444', u'CHEMBL1475944', u'CHEMBL542160', u'CHEMBL556385', u'CHEMBL561333', u'CHEMBL1367834', u'CHEMBL239670', u'CHEMBL1414483', u'CHEMBL108387', u'CHEMBL1345148', u'CHEMBL591489', u'CHEMBL1508064', u'CHEMBL325205', u'CHEMBL1578570', u'CHEMBL524911', u'CHEMBL1570410', u'CHEMBL1422546', u'CHEMBL1934375', u'CHEMBL1549884', u'CHEMBL2018140', u'CHEMBL1464892', u'CHEMBL175201', u'CHEMBL573796', u'CHEMBL492531', u'CHEMBL2368254', u'CHEMBL532784', u'CHEMBL2360750', u'CHEMBL1397196', u'CHEMBL1352443', u'CHEMBL1627413', u'CHEMBL380917', u'CHEMBL230922', u'CHEMBL105512', u'CHEMBL2017833', u'CHEMBL1900518', u'CHEMBL1364853', u'CHEMBL1090210', u'CHEMBL184568', u'CHEMBL426572', u'CHEMBL451', u'CHEMBL1349580', u'CHEMBL1921936', u'CHEMBL1879695', u'CHEMBL232284', u'CHEMBL1609419', u'CHEMBL604338', u'CHEMBL53088', u'CHEMBL1376570', u'CHEMBL167879', u'CHEMBL1347728', u'CHEMBL2009986', u'CHEMBL1900919', u'CHEMBL551224', u'CHEMBL223428', u'CHEMBL1313490', u'CHEMBL57577', u'CHEMBL2110737', u'CHEMBL1529002', u'CHEMBL1411791', u'CHEMBL1412057', u'CHEMBL204513', u'CHEMBL1971295', u'CHEMBL54775', u'CHEMBL1404895', u'CHEMBL1194587', u'CHEMBL2337007', u'CHEMBL1910606', u'CHEMBL2347958', u'CHEMBL2146527', u'CHEMBL355216', u'CHEMBL1542197', u'CHEMBL576130', u'CHEMBL2324818', u'CHEMBL532170', u'CHEMBL1590999', u'CHEMBL2426645', u'CHEMBL380525', u'CHEMBL1433613', u'CHEMBL437009', u'CHEMBL424519', u'CHEMBL32857', u'CHEMBL12559', u'CHEMBL451798', u'CHEMBL314715', u'CHEMBL1331158', u'CHEMBL1819563', u'CHEMBL1300753', u'CHEMBL1500837', u'CHEMBL1583823', u'CHEMBL2000056', u'CHEMBL421059', u'CHEMBL1516455', u'CHEMBL1907256', u'CHEMBL1514528', u'CHEMBL192284', u'CHEMBL1378674', u'CHEMBL458401', u'CHEMBL353086', u'CHEMBL1643522', u'CHEMBL74841', u'CHEMBL1672758', u'CHEMBL1488819', u'CHEMBL2431850', u'CHEMBL433520', u'CHEMBL169322', u'CHEMBL1476348', u'CHEMBL88288', u'CHEMBL407394', u'CHEMBL297533', u'CHEMBL1317110', u'CHEMBL1978680', u'CHEMBL1352104', u'CHEMBL603273', u'CHEMBL596646', u'CHEMBL285585']


def profile_mongodb():
    """"""
    from query import similarity2, similarity3, similarity4
    db = pymongo.MongoClient().chem
    for threshold in [0.75]:  # [0.95, 0.9, 0.85, 0.8, 0.7]:
        report = []
        times = []
        counts = []

        # Perform the queries
        for chembl_id in chembl_ids:
            print chembl_id
            qmol = db.molecules.find_one({'chembl_id': chembl_id})
            report.append('Query: {} - {}'.format(qmol['chembl_id'], qmol['smiles']))
            start = time.time()
            results = similarity4(qmol['mfp2']['bits'], threshold)
            end = time.time()
            counts.append(len(results))
            report.append('Results ({})'.format(len(results)))
            print report[-1]
            for r in results:
                report.append('{}: {}'.format(r['tanimoto'], r['chembl_id']))
                print report[-1]
            times.append(end - start)

        # Produce a report of the results
        report.append('Counts: {}'.format(' '.join(str(c) for c in counts)))
        report.append('Mean: {}'.format(np.mean(counts)))
        report.append('Median: {}'.format(np.median(counts)))
        report.append('Times: {}'.format(' '.join(str(t) for t in times)))
        report.append('Mean: {}'.format(np.mean(times)))
        report.append('Median: {}'.format(np.median(times)))
        report.append('95th Percentile: {}'.format(np.percentile(times, 95)))
        report = '\n'.join(report)
        print report
        with open('benchmarks/{}-{}-{}-{}.txt'.format('unfolded', 'agg', threshold, datetime.datetime.utcnow()), 'w') as f:
            f.write(report)

# You can profile individual queries using built in MongoDB profiling:
#db.set_profiling_level(pymongo.ALL)
#db.set_profiling_level(pymongo.OFF)
# But this isn't so useful for searches made up of multiple database queries (it will underestimate)


def profile_postgres():
    conn = psycopg2.connect("dbname=chembl user=matt")
    cur = conn.cursor()

    for threshold in [0.75]:  # [0.95, 0.9, 0.85, 0.8, 0.7]:
        report = []
        times = []
        counts = []
        cur.execute("set rdkit.tanimoto_threshold=%s;", (threshold,))
        for chembl_id in chembl_ids:
            # ARGH! The CHEMBL ID vs. molregno thing is a nightmare
            cur.execute("select entity_id from chembl_id_lookup where chembl_id = %s", (chembl_id,))
            molregno = cur.fetchone()[0]
            cur.execute("select m from rdk.mols where molregno = %s", (molregno,))
            smiles = cur.fetchone()[0]
            cur.execute("select mfp3 from rdk.fps where molregno = %s", (molregno,))
            qfp = cur.fetchone()[0]
            report.append('Query: {} - {}'.format(chembl_id, smiles))
            print chembl_id
            start = time.time()
            cur.execute("select molregno from rdk.fps where mfp3%%%s", (qfp,))
            #cur.execute("select molregno from rdk.fps where mfp%%morganbv_fp(%s)", (smiles,))
            results = cur.fetchall()
            end = time.time()
            counts.append(len(results))
            report.append('Results ({})'.format(len(results)))
            print report[-1]
            for r in results:
                cur.execute("select chembl_id from chembl_id_lookup where entity_type = 'COMPOUND' and entity_id = %s", (r,))
                report.append(cur.fetchone()[0])
                print report[-1]
            times.append(end - start)

        # Produce a report of the results
        report.append('Counts: {}'.format(' '.join(str(c) for c in counts)))
        report.append('Mean: {}'.format(np.mean(counts)))
        report.append('Median: {}'.format(np.median(counts)))
        report.append('Times: {}'.format(' '.join(str(t) for t in times)))
        report.append('Mean: {}'.format(np.mean(times)))
        report.append('Median: {}'.format(np.median(times)))
        report.append('95th Percentile: {}'.format(np.percentile(times, 95)))
        report = '\n'.join(report)
        print report
        with open('benchmarks/{}-{}-{}-{}.txt'.format('unfolded', 'postgres', threshold, datetime.datetime.utcnow()), 'w') as f:
            f.write(report)
    cur.close()
    conn.close()


if __name__ == '__main__':
    #choose_random()
    #profile_mongodb()
    profile_postgres()
