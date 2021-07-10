from selenium import webdriver
chrome_path="C:\Development\chromedriver.exe"
driver= webdriver.Chrome(executable_path=chrome_path)
driver.get("https://www.amazon.in/Amazon-Brand-Resistant-Mattress-Protector/dp/B07PXLXTCS/ref=sr_1_1?dchild=1&pd_rd_r=c5fe8fe8-3016-4765-b5c7-77144828caad&pd_rd_w=tUshq&pd_rd_wg=45lqL&pf_rd_p=ed3aadcb-38fd-42ac-85fd-4e4219ceeb25&pf_rd_r=86RS97PMPNJDH3B3CZ24&qid=1618157596&refinements=p_n_format_browse-bin%3A19560802031&s=kitchen&sr=1-1")
price=driver.find_element_by_id("priceblock_ourprice")
print(price.text)
product_name=driver.find_element_by_xpath("//span[@id='productTitle']")
print(product_name.text)

