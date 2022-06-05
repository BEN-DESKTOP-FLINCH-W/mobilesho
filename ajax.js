$(document).ready(function(){
    $('#insert_form').on("submit", function(event){  
      event.preventDefault();  
      if($('#pname').val() == "")  
      {  
      alert("product is required");  
      }  
      else if($('#pqty').val() == '')  
      {  
      alert("quantity is required");  
      }  
      else if($('#prdprice').val() == '')
      {  
      alert("price is required");  
      }
      else if($('#prdctg').val() == '')
      {  
      alert("category is required");  
      } 
      else 
      {  
      $.ajax({  
        url:"/insert",  
        method:"POST",  
        data:$('#insert_form').serialize(),  
        beforeSend:function(){  
        $('#insert').val("Inserting");  
        },  
        success:function(data){  
          if (data=='success')  {
          window.location.href = "/shop";   
        }
        
       }  
        
      });  
      }  
    });


    $('#discounts_form').on("submit", function(event){  
      event.preventDefault();  
      if($('#prodctname').val() == "")  
      {  
      alert("product is required");  
      }  
      else if($('#startdate').val() == '')  
      {  
      alert("start date is required");  
      }  
      else if($('#enddate').val() == '')
      {  
      alert("enddate is required");  
      }
      else 
      {  
      $.ajax({  
        url:"/discounts",  
        method:"POST",  
        data:$('#discounts_form').serialize(),  
        beforeSend:function(){  
        $('#submitdiscounts').val("Inserting");  
        },  
        success:function(data){  
          if (data=='success')  {
             
        }
        
       } 
      });  
      }  
    });

    
    $('#updateproducts').on("submit", function(event){  
        event.preventDefault();  
        if($('#updatename').val() == "")  
        {  
        alert("required");  
        }  
        else if($('#updateqty').val() == '')  
        {  
        alert("required");  
        }  
        else if($('#updateselling').val() == '')
        {  
        alert("required");  
        }
        else 
        {  
        $.ajax({  
          url:"/update",  
          method:"POST",  
          data:$('#updateproducts').serialize(),  
          beforeSend:function(){  
          $('#submit_update').val("updating");  
          },  
          success:function(data){  
            if (data=='success')  {
            window.location.href = "/shop";   
          }
          
         } 
        });  
        }  
      });

      $('#deleteproduct').on("submit", function(event){  
        event.preventDefault();  
        if($('#categorydeletename').val() == "")  
        {  
        alert("required");  
        }  
        else 
        {  
        $.ajax({  
          url:"/delete",  
          method:"POST",  
          data:$('#deleteproduct').serialize(),  
          beforeSend:function(){  
          $('#submit_delete').val("deleting");  
          },  
          success:function(data){  
            if (data=='success')  {
            window.location.href = "/shop";   
          }
          
         } 
        });  
        }  
      });

      $('#categoryedit_form').on("submit", function(event){  
        event.preventDefault();  
        if($('#categoryname').val() == "")  
        {  
        alert("required");  
        }  
        else 
        {  
        $.ajax({  
          url:"/categoryedit",  
          method:"POST",  
          data:$('#categoryedit_form').serialize(),  
          beforeSend:function(){  
          $('#submit_editcategory').val("updating");  
          },  
          success:function(data){  
            if (data=='success')  {
            window.location.href = "/shop";   
          }
          
         } 
        });  
        }  
      });

      $('#categorydelete_form').on("submit", function(event){  
        event.preventDefault();  
        if($('#categorydeletename').val() == "")  
        {  
        alert("required");  
        }  
        else 
        {  
        $.ajax({  
          url:"/categorydelete",  
          method:"POST",  
          data:$('#categorydelete_form').serialize(),  
          beforeSend:function(){  
          $('#submit_deletecategory').val("deleting");  
          },  
          success:function(data){  
            if (data=='success')  {
            window.location.href = "/shop";   
          }
          
         } 
        });  
        }  
      });

      $('#cartitems_form').on("submit", function(event){  
        event.preventDefault();  
        if($('#uname').val() == "")  
        {  
        alert("required");  
        }
        else 
        {  
        $.ajax({  
          url:"/customerorders",  
          method:"POST",  
          data:$('#cartitems_form').serialize(),  
          beforeSend:function(){  
          $('#submitcustomers').val("submiting");  
          },  
          success:function(data){  
            if (data=='success')  {
              window.location.reload()
             
          }
          
         } 
        });  
        }  
      });

      $('#category_add').on("submit", function(event){  
        event.preventDefault();  
        if($('#category_add_name').val() == "")  
        {  
        alert("required");  
        }  
        else 
        {  
        $.ajax({  
          url:"/addcategory",  
          method:"POST",  
          data:$('#category_add').serialize(),  
          beforeSend:function(){  
          $('#submit_add_category').val("adding");  
          },  
          success:function(data){  
            if (data=='success')  {
            window.location.href = "/shop";   
          }
          
         } 
        });  
        }  
      });


      $('#complete_order_form').on("submit", function(event){  
        event.preventDefault();  
        if($('#order_complete_id').val() == "")  
        {  
        alert("required");  
        }  
        if($('#order_complete_total').val() == "")  
        {  
        alert("required");  
        }  
        else 
        {  
        $.ajax({  
          url:"/complete",  
          method:"POST",  
          data:$('#complete_order_form').serialize(),  
          beforeSend:function(){  
          $('#submit_complete').val("completing");  
          },  
          success:function(data){  
            if (data=='success')  {
            window.location.href = "/shop";   
          }
          
         } 
        });  
        }  
      });

      
      
});
