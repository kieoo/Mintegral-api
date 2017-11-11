# -*- coding:utf-8 -*
#coding:utf-8
'''
Created on 2015年12月10日

@author: Linked
'''
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

from features.config import mongo_config
from features.dao.mongo_template import MongoTemplate
from features.dao.sql_template import SqlTemplate
from features.model import Base
from features.util.common_util import object_to_dict


class Offer(Base):

    __tablename__ = 'campaign_list'
    
    
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer)
    advertiser_id = Column(Integer)
    name = Column(String)
    app_name = Column(String)
    platform = Column(Integer)
    landing_type = Column(Integer)
    promote_url = Column(String)
    direct_url = Column(String)
    apk_url = Column(String)
    icon = Column(String)
    total_budget = Column(Integer)
    daily_budget = Column(Integer)
    left_total_budget = Column(Integer)
    cost_daily_budget = Column(Integer)
    daily_cap = Column(Integer)
    start_date = Column(Integer)
    end_date = Column(Integer)
    hours = Column(String)
    original_price = Column(String)
    price = Column(String)
    country = Column(String)
    status = Column(Integer)
    reason = Column(String)
    timestamp = Column(Integer)
    date = Column(Integer)
    weight = Column(Integer)
    flow = Column(Integer)
    network = Column(Integer)
    preview_url = Column(String)
    trace_app_id = Column(String)
    sdk_trace_app_id = Column(String)
    campaign_type = Column(Integer)
    special_type = Column(String)
    ctype = Column(Integer)
    network_cid = Column(String)
    operator = Column(String)
    device = Column(String)
    mobile_traffic = Column(String)
    os_version = Column(String)
    android_version = Column(String)
    appdesc = Column(String)
    appsize = Column(String)
    startrate = Column(String)
    category = Column(String)
    sub_category = Column(String)
    appinstall = Column(String)
    tag = Column(Integer)
    direct = Column(Integer)
    button = Column(String)
    update = Column(String)
    target_app_id = Column(String)
    source = Column(Integer)
    source_id = Column(String)
    pre_click = Column(Integer)
    pre_click_rate = Column(Integer)
    pre_click_interval = Column(Integer)
    jump_type = Column(Integer)
    direct_trace_app_id = Column(String)
    
    def __repr__(self):
        return "<Offer(id='%d', name='%s', app_name='%s', status='%d')>"\
                   % (self.id, self.name, self.app_name, self.status)


    def setOffer(self, offerDict):
        for (k, v) in offerDict.iteritems():
            setattr(self, k, v)
            

##########################################################
# session = SqlTemplate()
# for obj in session.selectList(Offer, {'id': 3339457}):
#     print(object_to_dict(obj))
#  
# mongo = MongoTemplate(host = mongo_config['host'],\
#                                   port = mongo_config['port'],\
#                                   db = mongo_config['db'])
# print(mongo.findOne('campaign', {'campaignId': 3339457}))