from flask import Flask, redirect, url_for, render_template,request,jsonify,json
from flask_mysql_connector import MySQL
import mysql.connector
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField 
from wtforms.validators import InputRequired,Email,Length
import sys
from datetime import timedelta
from werkzeug.security import generate_password_hash,check_password_hash
class LoginForm (FlaskForm):
    username=StringField('username',validators=[InputRequired(),Length(min=4,max=30)]) 
    password=StringField('password',validators=[InputRequired(),Length(min=4,max=30)])
    remember=BooleanField('remember me')
class Registerform (FlaskForm):
    email=StringField('email',validators=[InputRequired(),Length(min=16,max=30)]) 
    username=StringField('username',validators=[InputRequired(),Length(min=4,max=30)]) 
    password=StringField('password',validators=[InputRequired(),Length(min=4,max=30)])

app=Flask(__name__)

app.config['SECRET_KEY']='ben@4321'

app.permanent_session_lifetime=timedelta(minutes=1)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="5807",
  database="shopassistant"
)

#customer interface
mycursor2=mydb.cursor()





mycursor2.execute("SELECT PRODUCT_NAME,SUM(PRICE) AS COST FROM SHOP_ORDERS GROUP BY PRODUCT_NAME")
data=mycursor2.fetchall()




#mycursor8=mydb.cursor()
#mycursor8.execute("SELECT * FROM shop")
#myorders=mycursor8.fetchall()

#labels=[row[0] for row in myorders]
#print(labels)
#values=[row[2] for row in myorders]
#print(values)





mysql=MySQL(app)
Bootstrap(app)
"""
@app.route('/home',methods=["GET","POST"])
def home():
    if request.method=="POST":

        global myorders1
        myorders1={}
        item=request.form.getlist("order-item-title")
        quantity=request.form.getlist("qty")
        res = {item[i]: quantity[i] for i in range(len(item))}
        myorders1=myorders1+res
        mycursor3=mydb.cursor()
        for x,y in res.items():
            mycursor3.execute("SELECT SELLING_PRICE FROM stock WHERE ITEM='{}' ".format(x))
            itemprice =mycursor3.fetchone()
            mycursor3.execute("SELECT ITEM_ID FROM stock WHERE ITEM='{}' ".format(x))
            prodctid =mycursor3.fetchone()
            mycursor3.execute("SELECT QUANTITY_IN_STOCK FROM stock WHERE ITEM='{}' ".format(x))
            prodctquantity =mycursor3.fetchone()
            newqty=abs(int(y)-int(prodctquantity[0]))
            mycursor3.execute("UPDATE stock SET  QUANTITY_IN_STOCK= {} WHERE ITEM = '{}'".format(int(newqty),x))
            mydb.commit()
            prodctid=prodctid[0]
            price=int(itemprice[0]) * int(y)
            mycursor3.execute( "INSERT INTO SHOP_ORDERS(PRODUCT_ID,PRODUCT_NAME,QUANTITY,PRICE)VALUES({},'{}',{},{})".format(int(prodctid),x,int(y),int(price)))
            mydb.commit()
            #orders
        
    return render_template('index.html',products=products)
    """

@app.route('/cornershop')
def resturant():
    return render_template('try.html')


@app.route('/insert',methods=["POST"])
def insert():
    if request.method=="POST":
        newitem=request.form.get("newproduct")
        newquantity=request.form.get("newprdqty")
        newsellingprice=request.form.get("newprice")
        prodcategory=request.form.get("newcategory")
        mycursor5=mydb.cursor()
        mycursor5.execute( "INSERT INTO stock(ITEM,QUANTITY_IN_STOCK,SELLING_PRICE,category)VALUES('{}',{},{},'{}')".format(newitem,int(newquantity),int(newsellingprice),prodcategory))
        mydb.commit()
    return jsonify('success')

@app.route('/customerproducts',methods=["GET","POST"])
def customerproducts():
    mycategory=mydb.cursor()
    mycategory.execute("SELECT category_name FROM categories")
    categories=mycategory.fetchall()
    mycustomers=[]
    for x in categories:
        x=x[0]
        mycurs=mydb.cursor()
        mycurs.execute("SELECT ITEM,SELLING_PRICE FROM stock where category='{}'".format(x))
        ctgs=mycurs.fetchall()
        mycustomers.append(ctgs)
    print(mycustomers)

    return "bena"



@app.route('/shop',methods=["GET","POST"])
def shop():
    analysis=mydb.cursor()
    analysis.execute("select sum(customer_orders.price) as price, customer_orders.category as category from complete_orders inner join customer_orders on complete_orders.order_id=customer_orders.customer_id group by category;")
    shopanalysis=analysis.fetchall()
    labels=[row[1] for row in shopanalysis]
    values=[int(row[0]) for row in shopanalysis]
   

    
    myordersx=mydb.cursor()
    myordersx.execute("select complete_orders.order_id as orderid, customer_orders.product_name as product, customer_orders.quantity as quantity, customer_orders.price as price, customer_orders.category as category from complete_orders inner join customer_orders on complete_orders.order_id=customer_orders.customer_id")
    myorders= myordersx.fetchall()

    mycategory=mydb.cursor()
    mycategory.execute("SELECT category_name FROM categories")
    global categories
    categories=mycategory.fetchall()

    mydicounts=mydb.cursor()
    mydicounts.execute("SELECT * FROM discounts")
    mydiscount=mydicounts.fetchall()

    mycursor2=mydb.cursor()
    mycursor2.execute("SELECT ITEM,SELLING_PRICE FROM stock")
    global products
    products=mycursor2.fetchall()

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM stock")
    mystock = mycursor.fetchall()

    myrecents=mydb.cursor()
    myrecents.execute("select * from totals")
    recents=myrecents.fetchall()

    myrecents.execute("select order_id from totals")
    orderids=myrecents.fetchall()
    array1=[]
    for order in orderids:
        order=order[0]
        myrecents.execute("select product,quantity from recent_orders where order_id='{}'".format(order))
        items=myrecents.fetchall()
        array1.append(items)
    print(array1)
    return render_template('shopowner.html',shopanalysis=shopanalysis,mystock=mystock,myorders=myorders,labels=labels,values=values,categories=categories,incomplete=recents,mydiscount=mydiscount,array1=array1)


@app.route('/customer',methods=["GET","POST"])
def bootstrap():
    mycategory=mydb.cursor()
    mycategory.execute("SELECT category_name FROM categories")
    categories=mycategory.fetchall()
    mycustomers=[]
    for x in categories:
        x=x[0]
        mycurs=mydb.cursor()
        mycurs.execute("SELECT ITEM,SELLING_PRICE FROM stock where category='{}'".format(x))
        ctgs=mycurs.fetchall()
        mycustomers.append(ctgs)
    
    
    return render_template('bootstrap.html',mycustomers=mycustomers,categories=categories)

@app.route('/customerorders',methods=["POST"])
def customerorders():
    if request.method=="POST":
        customername=request.form.get("uname")
        customer_total=request.form.get("customer_total")
        item=request.form.getlist("order-item-title")
        quantity=request.form.getlist("qty")
        res = {item[i]: quantity[i] for i in range(len(item))}
        print(res)
        for x,y in res.items():
            mycursor3=mydb.cursor()
            mycursor3.execute("SELECT SELLING_PRICE FROM stock WHERE ITEM='{}' ".format(x))
            itemprice =mycursor3.fetchone()

            mycursorq=mydb.cursor()
            mycursorq.execute("SELECT category FROM stock WHERE ITEM='{}' ".format(x))
            itemcategory =mycursorq.fetchone()
            itemcategory=itemcategory[0]
            #mycursor3.execute("SELECT ITEM_ID FROM stock WHERE ITEM='{}' ".format(x))
            #prodctid =mycursor3.fetchone()
            #mycursor3.execute("SELECT QUANTITY_IN_STOCK FROM stock WHERE ITEM='{}' ".format(x))
            #prodctquantity =mycursor3.fetchone()
            #newqty=abs(int(y)-int(prodctquantity[0]))
            #mycursor3.execute("UPDATE stock SET  QUANTITY_IN_STOCK= {} WHERE ITEM = '{}'".format(int(newqty),x))
            #mydb.commit()
            #prodctid=prodctid[0]
            price=int(itemprice[0]) * int(y)
            mycursor3.execute( "INSERT INTO customer_orders(customer_id,product_name,quantity,price,category)VALUES('{}','{}',{},{},'{}')".format(customername,x,int(y),int(price),itemcategory))
            mydb.commit()
            #orders
        mycursz=mydb.cursor()
        mycursz.execute("INSERT INTO totals(order_id,total) values('{}',{})".format(customername,customer_total))
        mydb.commit()
        
        return jsonify('success')

@app.route('/complete',methods=["GET","POST"])
def complete():
    if request.method=="POST":
        order_id=request.form.get("order_complete_id")
        order_total=request.form.get("order_complete_total")
        mycursorx=mydb.cursor()
        mycursorx.execute( "INSERT INTO complete_orders(order_id,total)VALUES('{}',{})".format(order_id,order_total))
        mydb.commit()
        mycursory=mydb.cursor()
        mycursory.execute( "DELETE from totals where order_id='{}'".format(order_id))
        mydb.commit()
        return jsonify('success')



@app.route('/discounts',methods=["POST"])
def discounts():
    if request.method=="POST":
        discountprod=request.form.get("dscprod")
        startdate=request.form.get("start_date")
        enddate=request.form.get("end_date")
        mycursor6=mydb.cursor()
        mycursor6.execute( "INSERT INTO discounts(Discounted_product,start_date,End_date)VALUES('{}','{}','{}')".format(discountprod,startdate,enddate))
        mydb.commit()
        return jsonify('success')

@app.route('/update',methods=["POST"])
def update():
    if request.method=="POST":
        itemid=request.form.get("productid")
        updateitem=request.form.get("updatename")
        updatequantity=request.form.get("updateqty")
        updateselling=request.form.get("updateselling")
        mycursor6=mydb.cursor()
        mycursor6.execute( "UPDATE stock set item='{}',quantity_in_stock={},selling_price={} where item_id={}".format(updateitem,updatequantity,updateselling,itemid))
        mydb.commit()
        return jsonify('success')


@app.route('/delete',methods=["POST"])
def delete():
    if request.method=="POST":
        deleteitemid=request.form.get("productdeleteid")
        mycursor6=mydb.cursor()
        mycursor6.execute( "DELETE from stock where item_id={}".format(deleteitemid))
        mydb.commit()
        return jsonify('success')


@app.route('/categoryedit',methods=["POST"])
def categoryedit():
    if request.method=="POST":
        categoryname=request.form.get("categoryname")
        categorynameid=request.form.get("categorynameid")
        mycursor6=mydb.cursor()
        mycursor6.execute( "UPDATE categories set category_name='{}' where category_name='{}'".format(categoryname,categorynameid))
        mydb.commit()
        return jsonify('success')


@app.route('/categorydelete',methods=["GET","POST"])
def categorydelete():
    if request.method=="POST":
        categorynameid=request.form.get("categorydeletenameid")
        mycursor6=mydb.cursor()
        mycursor6.execute( "Delete from categories where category_name='{}'".format(categorynameid))
        mydb.commit()
        return jsonify('success')


@app.route('/stocks',methods=["GET","POST"])
def stocks():
    if request.method=="POST":
        newitem=request.form.get("newproduct")
        newquantity=request.form.get("newprice")
        newsellingprice=request.form.get("newsell-price")
        remitem=request.form.get("rem-prod-name")
        changeqty=request.form.get("new_qty")
        changeitem=request.form.get("changeprod-name")
        changesellprice=request.form.get("changeprod-price")
        itemtochangeprice=request.form.get("newchange_price")
        if newitem !=None:
            mycursor5=mydb.cursor()
            mycursor5.execute( "INSERT INTO stock(ITEM,QUANTITY_IN_STOCK,SELLING_PRICE)VALUES('{}',{},{})".format(newitem,int(newquantity),int(newsellingprice)))
            mydb.commit()
        elif remitem !=None:
            mycursor6=mydb.cursor()
            mycursor6.execute("DELETE FROM stock WHERE ITEM = '{}'".format(remitem))
            mydb.commit()
        elif changeitem !=None:
            mycursor7=mydb.cursor()
            mycursor7.execute("UPDATE stock SET  QUANTITY_IN_STOCK= {} WHERE ITEM = '{}'".format(int(changeqty),changeitem))
            mydb.commit()
        elif changesellprice !=None:
            mycursor8=mydb.cursor()
            mycursor8.execute("UPDATE stock SET  SELLING_PRICE= {} WHERE ITEM = '{}'".format(int(itemtochangeprice),changesellprice))
            mydb.commit()


    return render_template('stocks.html', mystock=mystock)

@app.route('/orders',methods=["GET","POST"])
def orders():
    mycursor8=mydb.cursor()
    mycursor8.execute("SELECT * FROM SHOP_ORDERS")
    myorders = mycursor8.fetchall()
    if request.method=="POST":
        date_filter=request.form.get("filterdate")
        prdct=request.form.get("prod-id")
        filtrord=request.form.get("ord-no")
        print(myorders)
        if date_filter !=None:
            mycursor8.execute("SELECT * FROM SHOP_ORDERS WHERE DATE='{}' ".format(date_filter))
            myorders =mycursor8.fetchall()
        elif prdct !=None:
            mycursor8.execute("SELECT * FROM SHOP_ORDERS WHERE PRODUCT_ID='{}' ".format(prdct))
            myorders =mycursor8.fetchall()
        elif filtrord !=None:
            mycursor8.execute("SELECT * FROM SHOP_ORDERS WHERE ORDER_NUMBER='{}' ".format(filtrord))
            myorders =mycursor8.fetchall()
    return render_template('orders.html',myorders=myorders)

@app.route('/addcategory',methods=["GET","POST"])
def addcategory():
    if request.method=="POST":
        category=request.form.get("category_add_name")
        cursor=mydb.cursor()
        cursor.execute("INSERT INTO categories(category_name) values('{}')".format(category))
        mydb.commit()
        return jsonify('success')


@app.route('/page')
def analysis():
    return render_template('page.html')


if __name__ == "__main__":
    app.run(debug=True)
