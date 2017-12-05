# new feature
# Tags: optional

Feature: hehave learn TEST
"""
  内置key名：
  'Model'
  'Data'
  'Request_url'
  'Method'
  'Input'
  'Output'
"""
@template
Scenario: [1-1-1]template
  Given 准备MYSQL数据:创建随机两个app，结果保存到xx_temp
  """
    {
      'Model': 'App',                                           # 数据库 template 类名
      # insert into app (user_id, channel_name,platform) value (,,,)
      'save_name':{                                             # 结果保存到 save_name
                'user_id': $__fun(get_user_info, 'id'),         # 调用函数get_user_info('id')
                'channel_name': $__fun(get_random_string, 5),   # 调用函数get_random_string(5)
                'platform' : 1,
        }

     }
  """
  Given 准备数据:创建
  """
  {
    'Data':{
         'app_id':['test', 'test_9999', '1234_test']           # 保存 ['test', 'test_9999', '1234_test'] 到 app_id
    }
  }
  """
  When 输入参数，验证返回 X3
  """
  {
   'Input':{
      # 参数化两种格式
      'id' : $__fun(get_save_info, 'save_name', 'id'),           # 参数化 获取刚刚插入的App 的 id
      'id' : ${save_name.id}                                     # 参数化 等价 上面的 $__fun(get_save_info
      'test_id' : ${app_id}                                      # 默认存在tmp_Data中 =  ${Tmp_Data.app_id}
    }
   'Output':{

      }
    }
  """
  Then 输入参数xxx，验证返回
  """
  {
    }
  """
  Then 检查MySql
  """
  {

    }
  """
  Then 检查mongo
  """
  {

    }
  """

