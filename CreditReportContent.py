import json
from collections import OrderedDict
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class CreditReportContent:

	def __init__(self, driver):
		self.dict = OrderedDict()
		self.dict_basic = OrderedDict()
		self.driver = driver
		self.driver.implicitly_wait(0)

	def run(self):
		self.info1(self.driver)
		self.info2(self.driver)
		self.info3(self.driver)
		self.info4(self.driver)
		self.info5(self.driver)
		self.info6(self.driver)
		self.info6_0(self.driver)
		self.info7(self.driver)
		self.info8(self.driver)
		self.info9(self.driver)
		# js = json.dumps(self.dict, ensure_ascii=False, indent=4, separators=(',', ':'))
		# print(js)
		return self.dict

	def info1(self,driver):
		try:
			tbody = driver.find_element_by_xpath('//*[@id="simpleheader"]/table/tbody')
			title = tbody.find_elements_by_xpath('./tr[1]/td/div/font')
			title = title[0].text + title[1].text
			dict1 = OrderedDict()
			k1 = tbody.find_element_by_xpath('./tr[3]/td[1]/div/font').text
			v1 = tbody.find_element_by_xpath('./tr[3]/td[2]/font').text
			dict1[k1]=v1
			k2 = tbody.find_element_by_xpath('./tr[3]/td[3]/div/font').text
			v2 = tbody.find_element_by_xpath('./tr[3]/td[4]/font').text
			dict1[k2] = v2
			k3 = tbody.find_element_by_xpath('./tr[4]/td[1]/div/font').text
			v3 = tbody.find_element_by_xpath('./tr[4]/td[2]/font').text
			dict1[k3] = v3
			k4 = tbody.find_element_by_xpath('./tr[4]/td[3]/div/font').text
			v4 = tbody.find_element_by_xpath('./tr[4]/td[4]/font	').text
			dict1[k4] = v4
			self.dict_basic[title] = dict1
		except:
			return
	# 基本信息
	#身份信息
	def info2(self,driver):
		keys = []
		values = []
		dict1 = OrderedDict()
		try:
			title_identity = driver.find_element_by_xpath("//*[text()='身份信息']").text
			tbody_tr = driver.find_elements_by_xpath("//*[text()='身份信息']/../../../../../following-sibling::table[1]/tbody/tr")
			for tr in tbody_tr:
				tds_k = tr.find_elements_by_xpath('./td[@class="tdStyle"]')
				tds_v = tr.find_elements_by_xpath('./td[@class="tdStyle1"]')
				for k in tds_k:
					key = k.find_element_by_xpath('./b').text.replace('\n', '')
					keys.append(key)
				for v in tds_v:
					val = v.find_element_by_xpath('./span').text
					values.append(val)
			for i in range(len(keys)):
				dict1[keys[i]]=values[i]
			self.dict_basic[title_identity]=dict1
		except:
			self.dict_basic['身份信息'] = dict1
			return
	#主要出资人信息
	def info3(self,driver):
		lists = []
		keys = []
		try:
			title_promoter = driver.find_element_by_xpath("//*[text()='主要出资人信息']").text
			#注册资金
			money = driver.find_element_by_xpath("//*[text()='主要出资人信息']/../../../following-sibling::tr[1]/td/b/font").text
			title_promoter = title_promoter+'('+money+')'
			tbody_trs = driver.find_elements_by_xpath("//*[text()='主要出资人信息']/../../../../../following-sibling::table[1]/tbody/tr")
			keys_td = tbody_trs[0].find_elements_by_xpath('./td')
			for key in keys_td:
				k = key.find_element_by_xpath('./b').text.replace('\n', '')
				keys.append(k)
			for tr in tbody_trs[1:]:
				dict1 = OrderedDict()
				values = []
				tds = tr.find_elements_by_xpath('./td')
				for td in tds:
					val = td.find_element_by_xpath('./span').text
					values.append(val)
				for i in range(len(keys)):
					dict1[keys[i]] = values[i]
				lists.append(dict1)
			self.dict_basic[title_promoter]=lists
		except:
			self.dict_basic['主要出资人信息'] = lists
			return
	# 高管人员信息
	def info4(self,driver):
		lists = []
		keys = []
		try:
			title_basic = driver.find_element_by_xpath("//*[text()='基本信息']").text
		except:
			self.dict['基本信息'] = lists
			return
		try:
			title_senior = driver.find_element_by_xpath("//*[text()='高管人员信息']").text
			tbody_trs = driver.find_elements_by_xpath("//*[text()='高管人员信息']/../../../../../following-sibling::table[1]/tbody/tr")
			keys_td = tbody_trs[0].find_elements_by_xpath('./td')
			for key in keys_td:
				k = key.find_element_by_xpath('./b').text.replace('\n', '')
				keys.append(k)
			for tr in tbody_trs[1:]:
				dict1 = OrderedDict()
				values = []
				tds = tr.find_elements_by_xpath('./td')
				for td in tds:
					val = td.find_element_by_xpath('./span').text
					values.append(val)
				for i in range(len(keys)):
					dict1[keys[i]] = values[i]
				lists.append(dict1)
			self.dict_basic[title_senior]=lists
			self.dict[title_basic]=self.dict_basic
		except:
			self.dict_basic['高管人员信息'] = lists
			self.dict[title_basic] = self.dict_basic
			return
	#有直接关联关系的其他企业
	def info5(self,driver):
		keys = []
		lists = []
		try:
			title_relation = driver.find_element_by_xpath("//*[text()='有直接关联关系的其他企业']").text
			tbody_keys = driver.find_elements_by_xpath("//*[text()='有直接关联关系的其他企业']/../../../../../following-sibling::table[1]/tbody/tr[1]/td")
			for key in tbody_keys:
				k = key.find_element_by_xpath('./b').text.replace('\n', '')
				keys.append(k)
			tbody_vals = driver.find_elements_by_xpath("//*[text()='有直接关联关系的其他企业']/../../../../../following-sibling::table[1]/tbody/tr[@height='25']")
			for val in tbody_vals:
				dict1 = OrderedDict()
				v1 = val.find_element_by_xpath('./td[1]//span').text
				dict1[keys[0]] = v1
				v2 = val.find_element_by_xpath('./td[2]').text
				dict1[keys[1]] = v2
				lists.append(dict1)
			self.dict[title_relation]=lists
		except:
			self.dict['有直接关联关系的其他企业'] = lists
			return
	#财务报表
	def info6(self,driver):
		#资产负债表,利润表,现金流量表
		dict2 = OrderedDict()
		try:
			title_finance = driver.find_element_by_xpath("//*[text()='财务报表']").text
		except:
			self.dict['财务报表'] = dict2
			return
		ll = ['资产负债表','利润表','现金流量表']
		for name in ll:
			lists = []
			keys = []
			try:
				title1 = driver.find_element_by_xpath("//*[contains(text(),'{}')]".format(name)).text
				tbody_trs = driver.find_elements_by_xpath("//*[contains(text(),'{}')]/../../../../../following-sibling::table[1]/tbody/tr".format(name))
				keys_td = tbody_trs[0].find_elements_by_xpath('./td')
				for key in keys_td:
					k = key.find_element_by_xpath('./b').text.replace('\n', '')
					keys.append(k)
				for tr in tbody_trs[1:]:
					dict1 = OrderedDict()
					values = []
					tds = tr.find_elements_by_xpath('./td')
					for td in tds:
						val = td.find_element_by_xpath('.//span').text
						values.append(val)
					for i in range(len(keys)):
						dict1[keys[i]] = values[i]
					lists.append(dict1)
				dict2[title1] = lists
			except:
				dict2[name] = lists
			# 添加财务报表字段
			self.dict[title_finance] = dict2
	#信息概要
	def info6_0(self,driver):
		dict = OrderedDict()
		try:
			title_info = driver.find_element_by_xpath("//*[text()='信息概要']").text
		except:
			self.dict['信息概要'] = dict
			return
		# 信息主体
		try:
			content = driver.find_element_by_xpath("//*[text()='信息概要']/../../../following-sibling::tr[2]/td/span").text.split('\n')
			dict['信息主体'] = content
		except:
			dict['信息主体'] = ''
		#未结清信贷信息概要
		self.info6_1(driver,dict)
		#已结清信贷信息概要
		self.info6_2(driver,dict)
		#负债变化历史
		lists = []
		try:
			title1 = driver.find_element_by_xpath("//*[text()='负债变化历史']").text
			for num in [0, 3, 6]:
				self.info6_3(driver, num, lists)
			dict[title1] = lists
		except:
			dict['负债变化历史'] = lists
			return
		#对外担保信息概要
		self.info6_4(driver,dict)
		self.dict[title_info]=dict

	def info6_1(self,driver,dict):
		lists = []
		keys = []
		try:
			title = driver.find_element_by_xpath("//*[text()='未结清信贷信息概要']").text
			tbody1 = driver.find_element_by_xpath("//*[text()='未结清信贷信息概要']/../../../../../following-sibling::table[1]/tbody")
		except:
			dict['未结清信贷信息概要'] = lists
			return
		
		
		try:
			# 由资产管理公司处置的债务
			b = tbody1.find_element_by_xpath('./tr[1]/td[1]/b').text
			b1 = tbody1.find_element_by_xpath('./tr[2]/td[1]/b').text+'('+b+')'
			b2 = tbody1.find_element_by_xpath('./tr[2]/td[2]/b').text+'('+b+')'
			b3 = tbody1.find_element_by_xpath('./tr[2]/td[3]/b').text+'('+b+')'
			keys.append(b1)
			keys.append(b2)
			keys.append(b3)
		except:
			pass
		
		
		try:
			#欠息汇总
			q = tbody1.find_element_by_xpath('./tr[1]/td[2]/b').text
			q1 = tbody1.find_element_by_xpath('./tr[2]/td[4]/b').text + '(' + q + ')'
			q2 = tbody1.find_element_by_xpath('./tr[2]/td[5]/b').text + '(' + q + ')'
			keys.append(q1)
			keys.append(q2)
		except:
			pass
		try:
			tbody_vals1 = tbody1.find_elements_by_xpath('./tr[@height="25"]')
			for tr in tbody_vals1:
				dict1 = OrderedDict()
				values = []
				tds = tr.find_elements_by_xpath('./td')
				for td in tds:
					val = td.find_element_by_xpath('./span').text
					values.append(val)
				for i in range(len(keys)):
					dict1[keys[i]] = values[i]
				lists.append(dict1)
		except:
			pass
		try:
			tbody2 = driver.find_element_by_xpath("//*[text()='未结清信贷信息概要']/../../../../../following-sibling::table[2]/tbody")
			keys = []
			# 垫款汇总
			t = tbody2.find_element_by_xpath('./tr[1]/td[1]/b').text
			t1 = tbody2.find_element_by_xpath('./tr[2]/td[1]/b').text + '(' + t + ')'
			t2 = tbody2.find_element_by_xpath('./tr[2]/td[2]/b').text + '(' + t + ')'
			keys.append(t1)
			keys.append(t2)
			# 担保代偿或第三方代偿的债务
			d = tbody2.find_element_by_xpath('./tr[1]/td[2]/b').text
			d1 = tbody2.find_element_by_xpath('./tr[2]/td[3]/b').text + '(' + d + ')'
			d2 = tbody2.find_element_by_xpath('./tr[2]/td[4]/b').text + '(' + d + ')'
			d3 = tbody2.find_element_by_xpath('./tr[2]/td[5]/b').text + '(' + d + ')'
			keys.append(d1)
			keys.append(d2)
			keys.append(d3)
			tbody_vals2 = tbody2.find_elements_by_xpath('./tr[@height="25"]')
			for tr in tbody_vals2:
				dict1 = OrderedDict()
				values = []
				tds = tr.find_elements_by_xpath('./td')
				for td in tds:
					val = td.find_element_by_xpath('./span').text
					values.append(val)
				for i in range(len(keys)):
					dict1[keys[i]] = values[i]
				lists.append(dict1)
		except:
			pass
		keys = ['类型']
		kk = []
		try:
			# 正常类汇总
			# z = tbody3.find_element_by_xpath('./tr[1]/td[2]/b').text
			# z1 = tbody3.find_element_by_xpath('./tr[2]/td[1]/b').text + '(' + z + ')'
			# z2 = tbody3.find_element_by_xpath('./tr[2]/td[2]/b').text + '(' + z + ')'
			z = driver.find_element_by_xpath("//*[text()='正常类汇总']").text
			z1 = '笔数'+ '(' + z + ')'
			z2 = '余额'+ '(' + z + ')'
			kk.append(z)
			keys.append(z1)
			keys.append(z2)
		except:
			pass
		try:
			# 关注类汇总
			# g = driver.find_element_by_xpath('/html/body/center/div/table[20]/tbody/tr[1]/td[3]/b').text
			# g1 = driver.find_element_by_xpath('/html/body/center/div/table[20]/tbody/tr[2]/td[3]/b').text + '(' + g + ')'
			# g2 = driver.find_element_by_xpath('/html/body/center/div/table[20]/tbody/tr[2]/td[4]/b').text + '(' + g + ')'
			g = driver.find_element_by_xpath("//*[text()='关注类汇总']").text
			g1 = '笔数' + '(' + g + ')'
			g2 = '余额' + '(' + g + ')'
			kk.append(g)
			keys.append(g1)
			keys.append(g2)
		except:
			pass
		try:
			# 不良/违约类汇总
			# w = driver.find_element_by_xpath('/html/body/center/div/table[20]/tbody/tr[1]/td[4]/b').text
			# w1 = driver.find_element_by_xpath('/html/body/center/div/table[20]/tbody/tr[2]/td[5]/b').text + '(' + w + ')'
			# w2 = driver.find_element_by_xpath('/html/body/center/div/table[20]/tbody/tr[2]/td[6]/b').text + '(' + w + ')'
			w = driver.find_element_by_xpath("//*[text()='不良/违约类汇总']").text
			w1 = '笔数' + '(' + w + ')'
			w2 = '余额' + '(' + w + ')'
			kk.append(w)
			keys.append(w1)
			keys.append(w2)
		except:
			pass
		try:
			# 合计
			# h = driver.find_element_by_xpath('/html/body/center/div/table[20]/tbody/tr[1]/td[5]/b').text
			# h1 = driver.find_element_by_xpath('/html/body/center/div/table[20]/tbody/tr[2]/td[6]/b').text + '(' + h + ')'
			# h2 = driver.find_element_by_xpath('/html/body/center/div/table[20]/tbody/tr[2]/td[7]/b').text + '(' + h + ')'
			h = driver.find_element_by_xpath("//*[text()='合计']").text
			h1 = '笔数' + '(' + h + ')'
			h2 = '余额' + '(' + h + ')'
			kk.append(h)
			keys.append(h1)
			keys.append(h2)
		except:
			pass
		if len(kk) > 0:
			try:
				tbody3 = driver.find_element_by_xpath("//*[text()='{}']".format(kk[0]))
				tbody_vals3 = tbody3.find_elements_by_xpath("../../../tr[@height='25']")
				for tr in tbody_vals3:
					dict1 = OrderedDict()
					values = []
					tds = tr.find_elements_by_xpath('./td')
					for td in tds:
						try:
							val = td.find_element_by_xpath('./b').text
						except:
							val = td.find_element_by_xpath('./span').text
						values.append(val)
					for i in range(len(keys)):
						dict1[keys[i]] = values[i]
					lists.append(dict1)
			except:
				pass
		dict[title] = lists
	def info6_2(self,driver,dict):
		lists = []
		keys = []
		try:
			title = driver.find_element_by_xpath("//*[text()='已结清信贷信息概要']").text
			tbody1 = driver.find_element_by_xpath("//*[text()='已结清信贷信息概要']/../../../../../following-sibling::table[1]/tbody")
		except:
			dict['已结清信贷信息概要'] = lists
			return
		try:
			#由资产管理公司处置的债务
			b = tbody1.find_element_by_xpath('./tr[1]/td[1]/b').text.replace('\n', '')
			b1 = tbody1.find_element_by_xpath('./tr[2]/td[1]/b').text.replace('\n', '')+'('+b+')'
			b2 = tbody1.find_element_by_xpath('./tr[2]/td[2]/b').text.replace('\n', '')+'('+b+')'
			b3 = tbody1.find_element_by_xpath('./tr[2]/td[3]/b').text.replace('\n', '')+'('+b+')'
			keys.append(b1)
			keys.append(b2)
			keys.append(b3)
		except:
			pass
		try:
			#被剥离负债汇总
			l = tbody1.find_element_by_xpath('./tr[1]/td[2]/b').text.replace('\n', '')
			l1 = tbody1.find_element_by_xpath('./tr[2]/td[4]/b').text.replace('\n', '')+'('+l+')'
			l2 = tbody1.find_element_by_xpath('./tr[2]/td[5]/b').text.replace('\n', '')+'('+l+')'
			l3 = tbody1.find_element_by_xpath('./tr[2]/td[6]/b').text.replace('\n', '')+'('+l+')'
			keys.append(l1)
			keys.append(l2)
			keys.append(l3)
		except:
			pass
		try:
			#欠息汇总
			q = tbody1.find_element_by_xpath('./tr[1]/td[3]/b').text.replace('\n', '')
			q1 = tbody1.find_element_by_xpath('./tr[2]/td[7]/b').text.replace('\n', '') + '(' + q + ')'
			q2 = tbody1.find_element_by_xpath('./tr[2]/td[8]/b').text.replace('\n', '') + '(' + q + ')'
			keys.append(q1)
			keys.append(q2)
		except:
			pass
		try:
			tbody_vals1 = tbody1.find_elements_by_xpath('./tr')
			for tr in tbody_vals1[2:]:
				dict1 = OrderedDict()
				values = []
				tds = tr.find_elements_by_xpath('./td')
				for td in tds:
					val = td.find_element_by_xpath('./span').text
					values.append(val)
				for i in range(len(keys)):
					dict1[keys[i]] = values[i]
				lists.append(dict1)
		except:
			pass
		try:
			tbody2 = driver.find_element_by_xpath("//*[text()='已结清信贷信息概要']/../../../../../following-sibling::table[2]/tbody")
			keys = []
			# 垫款汇总
			t = tbody2.find_element_by_xpath('./tr[1]/td[1]/b').text.replace('\n', '')
			t1 = tbody2.find_element_by_xpath('./tr[2]/td[1]/b').text.replace('\n', '') + '(' + t + ')'
			t2 = tbody2.find_element_by_xpath('./tr[2]/td[2]/b').text.replace('\n', '')+ '(' + t + ')'
			t3 = tbody2.find_element_by_xpath('./tr[2]/td[3]/b').text.replace('\n', '') + '(' + t + ')'
			keys.append(t1)
			keys.append(t2)
			keys.append(t3)
			# 担保代偿或第三方代偿的债务
			d = tbody2.find_element_by_xpath('./tr[1]/td[2]/b').text.replace('\n', '')
			d1 = tbody2.find_element_by_xpath('./tr[2]/td[4]/b').text.replace('\n', '') + '(' + d + ')'
			d2 = tbody2.find_element_by_xpath('./tr[2]/td[5]/b').text.replace('\n', '') + '(' + d + ')'
			d3 = tbody2.find_element_by_xpath('./tr[2]/td[6]/b').text.replace('\n', '') + '(' + d + ')'
			keys.append(d1)
			keys.append(d2)
			keys.append(d3)
			tbody_vals2 = tbody2.find_elements_by_xpath('./tr')
			for tr in tbody_vals2[2:]:
				dict1 = OrderedDict()
				values = []
				tds = tr.find_elements_by_xpath('./td')
				for td in tds:
					val = td.find_element_by_xpath('./span').text
					values.append(val)
				for i in range(len(keys)):
					dict1[keys[i]] = values[i]
				lists.append(dict1)
		except:
			pass
		try:
			tbody3 = driver.find_element_by_xpath("//*[text()='已结清信贷信息概要']/../../../../../following-sibling::table[3]/tbody")
			keys = ['类型']
			t_keys = tbody3.find_elements_by_xpath('./tr[1]/td[@align="center"]')
			for key in t_keys:
				k = key.find_element_by_xpath('./b').text.replace('\n', '')
				keys.append(k)
			tbody_vals3 = tbody3.find_elements_by_xpath('./tr')
			for tr in tbody_vals3[1:]:
				dict1 = OrderedDict()
				values = []
				tds = tr.find_elements_by_xpath('./td')
				for td in tds:
					try:
						val = td.find_element_by_xpath('./b').text
					except:
						val = td.find_element_by_xpath('./span').text
					values.append(val)
				for i in range(len(keys)):
					dict1[keys[i]] = values[i]
				lists.append(dict1)
		except:
			pass
		dict[title] = lists
	def info6_3(self,driver,num,lists):
		keys = ['类型']
		tbody_trs = driver.find_elements_by_xpath("//*[text()='负债变化历史']/../../../../../following-sibling::table[1]/tbody/tr")
		keys_td1 = tbody_trs[num].find_elements_by_xpath('./td')
		for key in keys_td1:
			try:
				k = key.find_element_by_xpath('./b').text.replace('\n', '')
				keys.append(k)
			except:
				pass
		for tr in tbody_trs[num+1:num+3]:
			dict1 = OrderedDict()
			values = []
			tds = tr.find_elements_by_xpath('./td')
			for td in tds:
				try:
					val = td.find_element_by_xpath('./b').text
				except:
					val = td.text
				values.append(val)
			for i in range(len(keys)):
				dict1[keys[i]] = values[i]
			lists.append(dict1)
	def info6_4(self,driver,dict):
		lists = []
		keys = ['类型']
		try:
			title = driver.find_element_by_xpath("//*[text()='对外担保信息概要']").text
			t_body = driver.find_element_by_xpath("//*[text()='对外担保信息概要']/../../../../../following-sibling::table[1]/tbody")
			trs = t_body.find_elements_by_xpath('./tr')
			k1 = t_body.find_element_by_xpath('./tr[1]/td[2]/b').text.replace('\n', '')
			k2 = t_body.find_element_by_xpath('./tr[1]/td[3]/b').text.replace('\n', '')
			k = t_body.find_element_by_xpath('./tr[1]/td[4]/b').text.replace('\n', '')
			k3 = t_body.find_element_by_xpath('./tr[2]/td[1]/b').text+'('+k+')'
			k4 = t_body.find_element_by_xpath('./tr[2]/td[2]/b').text+'('+k+')'
			k5 = t_body.find_element_by_xpath('./tr[2]/td[3]/b').text+'('+k+')'
			k6 = t_body.find_element_by_xpath('./tr[2]/td[4]/b').text+'('+k+')'
			keys.append(k1)
			keys.append(k2)
			keys.append(k3)
			keys.append(k4)
			keys.append(k5)
			for tr in trs[2:]:
				dict1 = OrderedDict()
				vals = []
				tds = tr.find_elements_by_xpath('./td')
				for td in tds:
					try:
						val = td.find_element_by_xpath('./b').text
					except:
						val = td.find_element_by_xpath('./span').text
					vals.append(val)
				for i in range(len(keys)):
					dict1[keys[i]]=vals[i]
				lists.append(dict1)
			dict[title] = lists
		except:
			dict['对外担保信息概要'] = lists

	#信贷记录明细
	def info7(self,driver):
		dict = OrderedDict()
		try:
			title1 = driver.find_element_by_xpath("//*[text()='信贷记录明细']").text
		except:
			self.dict['信贷记录明细'] = dict
			return
		nums = []
		for i in range(20):
			if i % 2 != 0:
				nums.append(i)
		#未结清业务
		for num in nums:
			num = self.info7_1(driver,dict,num)
			if num == 0:
				break
		#不良和违约类
		for num in nums:
			num = self.info7_2(driver,dict,num)
			if num == 0:
				break
		#关注类
		for num in nums:
			num = self.info7_3(driver,dict,num)
			if num == 0:
				break
		#正常类
		for num in nums:
			num = self.info7_4(driver,dict,num)
			if num == 0:
				break
		#已结清业务
		for num in nums:
			num = self.info7_5(driver,dict,num)
			if num == 0:
				break
		self.dict[title1]=dict

	def info7_1(self,driver,dict,num):
		lists = []
		keys = []
		try:
			title2 = driver.find_element_by_xpath("//*[text()='未结清业务']").text
			title3 = driver.find_element_by_xpath("//*[text()='未结清业务']/../../../../../following-sibling::table[{}]/tbody/tr//font".format(num)).text
			title = title2+'/'+title3
			tbody_trs = driver.find_elements_by_xpath("//*[text()='未结清业务']/../../../../../following-sibling::table[{}]/tbody/tr".format(num+1))
			keys_td0 = tbody_trs[0].find_elements_by_xpath('./td')
			keys_td1 = tbody_trs[1].find_elements_by_xpath('./td')
			if title3 == '银行承兑汇票':
				number = 2
				for key in keys_td0[:2]:
					k = key.find_element_by_xpath('./b').text.replace('\n', '')
					keys.append(k)
				for key in keys_td1:
					k = key.find_element_by_xpath('./b').text.replace('\n', '')
					keys.append(k)
				keys.append(keys_td0[-1].find_element_by_xpath('./b').text.replace('\n', ''))
			else:
				number = 1
				for key in keys_td0:
					k = key.find_element_by_xpath('./b').text.replace('\n', '')
					keys.append(k)
			for tr in tbody_trs[number:]:
				dict1 = OrderedDict()
				values = []
				tds = tr.find_elements_by_xpath('./td')
				for td in tds:
					val = td.find_element_by_xpath('.//span').text
					values.append(val)
				for i in range(len(values)):
					dict1[keys[i]] = values[i]
				lists.append(dict1)
			dict[title] = lists
		except:
			dict['未结清业务'] = lists
			num = 0
			return num
	def info7_2(self,driver,dict,num):
		lists = []
		keys = []
		try:
			title2 = driver.find_element_by_xpath("//*[text()='不良和违约类']").text
			title3 = driver.find_element_by_xpath("//*[text()='不良和违约类']/../../../../../following-sibling::table[{}]/tbody/tr//font".format(num)).text
			title = title2+'/'+title3
			tbody_trs = driver.find_elements_by_xpath("//*[text()='不良和违约类']/../../../../../following-sibling::table[{}]/tbody/tr".format(num+1))
		except:
			dict['不良和违约类'] = lists
			num = 0
			return num
		try:
			keys_td0 = tbody_trs[0].find_elements_by_xpath('./td')
			for key in keys_td0:
				k = key.find_element_by_xpath('./b').text.replace('\n', '')
				keys.append(k)
			for tr in tbody_trs[1:]:
				dict1 = OrderedDict()
				values = []
				tds = tr.find_elements_by_xpath('./td')
				for td in tds:
					val = td.find_element_by_xpath('.//span').text
					values.append(val)
				for i in range(len(values)):
					dict1[keys[i]] = values[i]
				lists.append(dict1)
			dict[title] = lists
		except:
			dict[title] = lists
			num = 0
			return num
	def info7_3(self,driver,dict,num):
		lists = []
		keys = []
		try:
			title2 = driver.find_element_by_xpath("//*[text()='关注类']").text
			title3 = driver.find_element_by_xpath("//*[text()='关注类']/../../../../../following-sibling::table[{}]/tbody/tr//font".format(num)).text
			title = title2+'/'+title3
			tbody_trs = driver.find_elements_by_xpath("//*[text()='关注类']/../../../../../following-sibling::table[{}]/tbody/tr".format(num+1))
		except:
			dict['关注类'] = lists
			num = 0
			return num
		try:
			keys_td0 = tbody_trs[0].find_elements_by_xpath('./td')
			for key in keys_td0:
				k = key.find_element_by_xpath('./b').text.replace('\n', '')
				keys.append(k)
			for tr in tbody_trs[1:]:
				dict1 = OrderedDict()
				values = []
				tds = tr.find_elements_by_xpath('./td')
				for td in tds:
					val = td.find_element_by_xpath('.//span').text
					values.append(val)
				for i in range(len(keys)):
					dict1[keys[i]] = values[i]
				lists.append(dict1)
			dict[title] = lists
		except:
			dict[title] = lists
			num = 0
			return num
	def info7_4(self,driver,dict,num):
		lists = []
		keys = []
		try:
			title2 = driver.find_element_by_xpath("//*[text()='正常类']").text
		except:
			dict['正常类'] = lists
			num = 0
			return num
		try:
			if num == 1:
				title3 = driver.find_element_by_xpath("//*[text()='正常类']/../../../../../following-sibling::table[{}]/tbody/tr//font".format(num)).text
			else:
				num += 1
				title3 = driver.find_element_by_xpath("//*[text()='正常类']/../../../../../following-sibling::table[{}]/tbody/tr//font".format(num)).text
			title = title2+'/'+title3
			tbody_trs = driver.find_elements_by_xpath("//*[text()='正常类']/../../../../../following-sibling::table[{}]/tbody/tr".format(num + 1))
		except:
			num = 0
			return num
		try:
			keys_td0 = tbody_trs[0].find_elements_by_xpath('./td')
			keys_td1 = tbody_trs[1].find_elements_by_xpath('./td')
			if title3 == '银行承兑汇票':
				number = 2
				for key in keys_td0[:2]:
					k = key.find_element_by_xpath('./b').text.replace('\n', '')
					keys.append(k)
				for key in keys_td1:
					k = key.find_element_by_xpath('./b').text.replace('\n', '')
					keys.append(k)
				keys.append(keys_td0[-1].find_element_by_xpath('./b').text.replace('\n', ''))
			else:
				number = 1
				for key in keys_td0:
					k = key.find_element_by_xpath('./b').text.replace('\n', '')
					keys.append(k)
			for tr in tbody_trs[number:]:
				dict1 = OrderedDict()
				values = []
				tds = tr.find_elements_by_xpath('./td')
				for td in tds:
					val = td.find_element_by_xpath('.//span').text
					values.append(val)
				for i in range(len(values)):
					dict1[keys[i]] = values[i]
				lists.append(dict1)
			dict[title] = lists
		except:
			dict[title] = lists
			num = 0
			return num
	def info7_5(self,driver,dict,num):
		lists = []
		keys = []
		try:
			title2 = driver.find_element_by_xpath("//*[text()='已结清业务']").text
		except:
			dict['已结清业务'] = lists
			num = 0
			return num
		try:
			if num == 1:
				title3 = driver.find_element_by_xpath("//*[text()='已结清业务']/../../../../../following-sibling::table[{}]/tbody/tr//font".format(num)).text
			else:
				num += 1
				title3 = driver.find_element_by_xpath("//*[text()='已结清业务']/../../../../../following-sibling::table[{}]/tbody/tr//font".format(num)).text
			title = title2+'/'+title3
			tbody_trs = driver.find_elements_by_xpath("//*[text()='已结清业务']/../../../../../following-sibling::table[{}]/tbody/tr".format(num + 1))
		except:
			num = 0
			return num
		try:
			keys_td = tbody_trs[0].find_elements_by_xpath('./td')
			for key in keys_td:
				k = key.find_element_by_xpath('./b').text.replace('\n', '')
				keys.append(k)
			for tr in tbody_trs[1:]:
				dict1 = OrderedDict()
				values = []
				tds = tr.find_elements_by_xpath('./td')
				for td in tds:
					val = td.find_element_by_xpath('.//span').text
					values.append(val)
				for i in range(len(keys)):
					dict1[keys[i]] = values[i]
				lists.append(dict1)
			dict[title] = lists
		except:
			dict[title] = lists
			num = 0
			return num
	#公共信息明细
	def info8(self,driver):
		lists = []
		keys = []
		values = []
		dict = OrderedDict()
		dict1 = OrderedDict()
		try:
			title1 = driver.find_element_by_xpath("//*[text()='公共信息明细']").text
			title2 = driver.find_element_by_xpath("//*[text()='强制执行记录']").text
			tbody_trs = driver.find_element_by_xpath("//*[text()='强制执行记录']/../../../../../following-sibling::table[{}]/tbody/tr").text
			for tr in tbody_trs:
				tds = tr.find_elements_by_xpath('./td')
				for td in tds:
					key = td.find_element_by_xpath('./b').text.split(': ')[0]
					val = td.find_element_by_xpath('./span').text
					keys.append(key)
					values.append(val)
				for i in range(len(keys)):
					dict1[keys[i]] = values[i]
			lists.append(dict1)
			dict[title2] = lists
			self.dict[title1] = dict
		except:
			self.dict['公共信息明细'] = dict

	#声明信息明细
	def info9(self,driver):
		lists = []
		keys = []
		dict = OrderedDict()
		try:
			title1 = driver.find_element_by_xpath("//*[text()='声明信息明细']").text
			title2 = driver.find_element_by_xpath("//*[text()='报数机构说明']").text
			tbody_trs = driver.find_element_by_xpath("//*[text()='报数机构说明']/../../../../../following-sibling::table[{}]/tbody/tr").text
			keys_td = tbody_trs[0].find_elements_by_xpath('./td')
			for key in keys_td:
				k = key.find_element_by_xpath('./b').text
				keys.append(k)
			for tr in tbody_trs[1:]:
				dict1 = OrderedDict()
				values = []
				tds = tr.find_elements_by_xpath('./td')
				for td in tds:
					val = td.find_element_by_xpath('./span').text
					values.append(val)
				for i in range(len(keys)):
					dict1[keys[i]] = values[i]
				lists.append(dict1)
			dict[title2] = lists
			self.dict[title1] = dict
		except:
			self.dict['声明信息明细'] = dict


