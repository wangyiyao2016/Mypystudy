#!/usr/bin/env python
#coding=utf-8

"""
          斯巴达Python基础入门阶段结业 之 数据分析和数据挖掘 项目大习题
================================================

文件夹里有一个微博数据挖掘的片段文本内容(t.txt)，每一行则是一条微博，下面有该微博内容的相关字段信息。

对应字段如下（每一个逗号分隔的，数据在“”内的，则是字段的详细信息。空白则说明该对应字段没有内容。)
-----------------------------------------------------------------------------------------------------------------
bid    消息ID 
uid     用户ID 
username 用户名  
ugrade 用户等级字段 
content(text) 微博内容
img(message包含图片链接) 
created_at 微博发布时间 
source(来源)
rt_num, 转发数量 
cm_num, 评论数 
rt_uid, 转发UID
rt_username, 转发用户名
rt_v_class, 转发者等级 
rt_content, 转发内容 
rt_img, 转发内容所涉及图片 
src_rt_num, 源微博回复数 
src_cm_num, 源微博评论数 
gender,(用户性别) 
rt_mid（转发mid） 
geo 地区
lat() 经度
lon 纬度
place 地点
hashtags 
ats  @谁 
rt_hashtags, 回复标签
rt_ats, 回复@谁
v_url, 源微博URL 
rt_v_url 转发URL 

-----------------------------------------------------------------------------------------------------------------

微博文本附件的排序格式如下：

(从左至右，从上至下，bid字段开始，rt_v_url结束)

bid,uid,username,v_class,content,img,time,source,rt_num,cm_num,rt_uid,rt_username,\
rt_v_class,rt_content,rt_img,src_rt_num,src_cm_num,gender,rt_mid,location,rt_mid,mid,lat,lon,\
lbs_type,lbs_title,poiid,links,hashtags,ats,rt_links,rt_hashtags,rt_ats,v_url,rt_v_url

========================================================
"""

#习题开始 :)

"""
# 1. 首先，统计一下，这个微博的数据一共有多少行.
"""
with open('/home/jack/abc/Test/BigProject/t.txt','r') as f:
    f_content = f.readlines()
    f.seek(0)
    f_line = f.readline()
    f.seek(0)
    f_read = f.read()
#print f_content

#print f_line  
#print f_read.count('\n')    
#print f.read
#print len(f_content)


"""
# 2.该微博数据中，一共有多少个不重复的用户名.
"""
print f_line





"""
# 3.依次输出上面这些，用户名.
"""



"""
# 4.该微博数据中，有多少条是在2013年11月发布的.
"""




"""
# 5.该微博数据中，有哪些天的数据？（要求：排好序输出为一个list，例：['2013-03-04','2013-03-05']）
"""




"""
# 6.一共有多少天的数据?
"""





"""
# 7.该微博数据中，每个小时的发布量各是多少？(提示利用好字典类型)
"""






"""
# 8.该微博数据中，哪个小时的发布量最大？(可选题 ，需要lambda来排序)
"""





"""
# 9.请按照时间顺序输出 2013-11-03 每个小时的发布微博的频率,
      返回结果：[('00', 197), ('01', 184), ('02', 185), ('03', 220)] 等，
      要按顺序排好 :)
"""





"""
# 10. 统计这些数据里面，发布来源都是哪里的，并且输出他们各自的发布次数.

    1. 一共有多少个来源？

    2. 每个来源的发布次数，各是多少？

    3. 发布量最大的两个来源是用的什么设备？ (可选题，提示：会用到lambda来排序)
"""






"""
# 11.计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有多少个?
"""






"""
# 12.UID为573638104的用户 发了多少个微博.
"""






"""
# 13.该微博数据中，谁发的单条微博内容字数最多，输出这个用户的 用户名.
"""






"""
# 14.该微博数据中，谁转发的数量最多,输出用户的uid.
"""






"""
15.该文本里，11点钟，谁发的微博次数最多.
（要求：输出用户的uid，发微博最多次数同时有多人情况下，输出其中一位即可，主要看你的思路和方法）
"""







