if(document.readystate=='loading'){
    document.addEventListener('DOMContentLoaded',ready)
} else{
    ready()
}
function ready(){
    var removecartitems=document.getElementsByClassName('btn btn-danger')
    for(var i=0; i<removecartitems.length; i++){
        var button=removecartitems[i]
        button.addEventListener('click',removecartitem)
    }
    var quantityinputs=document.getElementsByClassName('cart-input-quantity')
    for(var i=0;i<quantityinputs.length; i++){
        var input=quantityinputs[i]
        input.addEventListener('change',quantitychanged)
    }
    var buttontoaddcart=document.getElementsByClassName('add-to-cart')
    for (var i=0;i<buttontoaddcart.length;i++){
        var button=buttontoaddcart[i]
        button.addEventListener('click',buttontoaddcartclicked)
    }


    var buttonaddtoproducts=document.getElementById('add-product-stock')
    buttonaddtoproducts.addEventListener('click',add_new_product)
    
    
    var removeproduct=document.getElementById('remove-product-stock')
    removeproduct.addEventListener('click',remove_prod)

    var changeprodqty=document.getElementById('change-quantity')
    changeprodqty.addEventListener('click',change_prod_qty)

    var changeprodqty=document.getElementById('change-product-sellprice')
    changeprodqty.addEventListener('click',change_sell_price)

    var oredrsbydate=document.getElementById('filter-date-order')
    oredrsbydate.addEventListener('click',filter_date_orders)

}
function filter_date_orders(){
    html='<span>\
    <h3>Enter Date</h3>\
    <label for="orddate">ORDER DATE:</label>\
    <input name="filterdate" id="orddate" type="date">\
    <input type="submit" value="show products" class="btn btn-success">\
    </span>'
    var myform =document.getElementById("form-date-filter")
    myform.innerHTML+=html
}

function filter_by_productid(){
    html='<div>\
    <h3>Enter Product Name</h3>\
    <label for="prodid">PRODUCT NAME:</label>\
    <input name="prod-id" id="prodid"type="text">\
    <input type="submit" value="show products" class="btn btn-success">\
    </div>'
    var myform =document.getElementById("form-prodid-filter")
    myform.innerHTML+=html
}

function filter_by_orderno(){
    html='<div>\
    <h3>Enter order number</h3>\
    <label for="ordno">ORDER NUMBER:</label>\
    <input name="ord-no" id="ordno" type="text">\
    <input type="submit" value="show products" class="btn btn-success">\
    </div>'
    var myform =document.getElementById("form-ordno-filter")
    myform.innerHTML+=html
}

function change_sell_price(){
    html='<span>\
    <h3>Enter Product to change Price</h3>\
    <input name="changeprod-price" type="text">\
    <input name="newchange_price" type="number">\
    <input type="submit" value="Change quantity" class="btn btn-success">\
    </span>'
    var form =document.getElementById("change-sell-price")
    form.innerHTML+=html
}


function change_prod_qty(){
    html='<span>\
    <h3>Enter Product to change quantity</h3>\
    <input name="changeprod-name" type="text">\
    <input name="new_qty" type="number">\
    <input type="submit" value="Change quantity" class="btn btn-success">\
    </span>'
    var form =document.getElementById("change-prod-qty")
    form.innerHTML+=html
}


function remove_prod(){
    html='<span>\
    <h3>Enter Product to Remove</h3>\
    <input name="rem-prod-name" type="text">\
    <input type="submit" value="REMOVE PRODUCT" class="btn btn-success">\
    </span>'
    var form =document.getElementById("remove-prod-form")
    form.innerHTML+=html
}


function add_new_product(){
    html='<div class="row">\
    <div>\
    <span>\
    <span><label for="newprdct">PRODUCT NAME:</label></span>\
    <span><input type="text" name="newproduct"id="newprdct"></span>\
    </div>\
    <div>\
    <label for="newqtystock">QUANTITY:</label>\
    <input type="number" name="newprice"id="newqtystock">\
    </div>\
    <div>\
    <label for="newprodsellprice">SELLING PRICE:</label>\
    <td><input type="text" name="newsell-price" id="newprodsellprice"></td>\
    </div>\
    <div>\
    <input type="submit" value="SUBMIT" class="btn btn-success">\
    </div>\
    </span>\
    </div>'
    var form =document.getElementById("add-product-form")
    form.innerHTML+=html
}



function buttontoaddcartclicked(event){
    var button=event.target
    var shopitem=button.parentElement.parentElement
    var title=shopitem.getElementsByClassName('item-title')[0].innerText
    var price=shopitem.getElementsByClassName('item-price')[0].innerText
    addtomycart(title,price)
    updateamount()
}
function addtomycart(title,price) {
    var cartrow=document.createElement('tr')
    cartrow.classList.add('cart-table')
    var cartitems=document.getElementsByClassName('cart-table')[0]
    var cartitemnames=cartitems.getElementsByClassName('cart-item title')
    for(var i=0; i<cartitemnames.length; i++) {
        if (cartitemnames[i].innerText==title){
            alert('already inserted')
            return
        }
    }
    var cartrowscontents=`
            <td><input name="order-item-title" class="form-control mb-2 mr-sm-2 cart-item title" value="${title}"readonly></td>
            <td><input class="form-control mb-2 mr-sm-2 cart-input-quantity" name="qty" type="number"value="1"></td>
            <td><input class="form-control mb-2 mr-sm-2 cart-price" name="pricecart" value="${price}"readonly></td>
            <td><button class=" btn btn-danger" type="button">REMOVE</button></td>`
    cartrow.innerHTML=cartrowscontents
    cartitems.append(cartrow)
    cartrow.getElementsByClassName('btn btn-danger')[0].addEventListener('click',removecartitem)
    cartrow.getElementsByClassName('cart-input-quantity')[0].addEventListener('change',quantitychanged)
}


function removecartitem(event) {
    var buttonclicked=event.target
    buttonclicked.parentElement.parentElement.remove()   
}

function quantitychanged(event) {
    var input=event.target
    if(isNaN(input.value) || input.value <=0 ){
        input.value=1
    }
    updateamount()


}


function updateamount() {
    var cartitemscontainer=document.getElementsByClassName('cart-items')[0] 
    var cartrows=cartitemscontainer.getElementsByTagName('tbody')
    for(var i=0;i<cartrows.length; i++) {
        var cartrow=cartrows[i]
        var priceelement=cartrow.getElementsByClassName("cart-price")[0].value
        console.log(priceelement)
        var quantityelement=cartrow.getElementsByClassName('cart-input-quantity')[0]
        var price=priceelement.innerText
        var quantity=quantityelement.value
        total=total + (price * quantity)
        console.log(total)
        document.getElementsByClassName("cart-price")[0].innerText=total
    }
}
