package com.example.personalityprediction;

import org.json.JSONObject;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class UserRegister extends Activity implements JsonResponse{

	EditText e1,e2,e3,e4,e5,e6,e7,e8;
	Button b1;
	String uname,passs,fname,lname,phonno,email,place,district;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_user_register);
		
		 e1=(EditText)findViewById(R.id.etfname);
	        e2=(EditText)findViewById(R.id.etlname);
	        e3=(EditText)findViewById(R.id.email);
	        e4=(EditText)findViewById(R.id.etphno);
	        e5=(EditText)findViewById(R.id.place);
	        e7=(EditText)findViewById(R.id.etuname);
	        e8=(EditText)findViewById(R.id.etpasss);
	        b1=(Button)findViewById(R.id.btregister);
	        
	        
			b1.setOnClickListener(new View.OnClickListener() {
				
				@Override
				public void onClick(View arg0) {
					// TODO Auto-generated method stub
					
					fname=e1.getText().toString();
					lname=e2.getText().toString();
					email=e3.getText().toString();
					phonno=e4.getText().toString();
					place=e5.getText().toString();
					uname=e7.getText().toString();
					passs=e8.getText().toString();
					
					
//					Toast.makeText(getApplicationContext(), "REGISTRATION SUCCESS",Toast.LENGTH_LONG).show();
//					startActivity(new Intent(getApplicationContext(),Login.class));
					if(fname.equalsIgnoreCase(""))
					{
					  e1.setError("please enter your first name");
					  e1.setFocusable(true);
					}
					else if(lname.equalsIgnoreCase(""))
					{
						e2.setError("please enter your last name");
						  e2.setFocusable(true);
					}
					
					else if(email.equalsIgnoreCase(""))
					{
						e3.setError("please enter email");
						  e3.setFocusable(true);
					}
					else if(phonno.equalsIgnoreCase("")&&phonno.length()!=10)
					{
						e4.setError("enter your phone no. in correct format");
						  e4.setFocusable(true);
					}
					else if(place.equalsIgnoreCase(""))
					{
						e5.setError("please enter your place");
						  e5.setFocusable(true);
					}

					else if(uname.equalsIgnoreCase(""))
					{
						e7.setError("please enter your username");
						e7.setFocusable(true);
					}
					else if(passs.equalsIgnoreCase("")&&passs.length()!=6)
					{
						e8.setError("please enter your password..Password should be 6 characters");
						  e8.setFocusable(true);
					}
					else
	{
					JsonReq JR=new JsonReq();
			        JR.json_response=(JsonResponse) UserRegister.this;
			        String q = "/userregister?fname="+fname+"&lname="+lname+"&phone="+phonno+"&email="+email+"&place="+place+"&uname="+uname+"&pass="+passs;
			        q=q.replace(" ","%20");
			        JR.execute(q);
	}
					

			
		

				}
			});
	}


	
	
	 public void response(JSONObject jo) {
			// TODO Auto-generated method stub
			try {
				String status=jo.getString("status");
				Log.d("pearl",status);
				
				
				if(status.equalsIgnoreCase("success")){
					
					
				 
					
				    
					 Toast.makeText(getApplicationContext(), "REGISTRATION SUCCESS", Toast.LENGTH_LONG).show();
					 startActivity(new Intent(getApplicationContext(),Login.class));
					 
				}
				else if(status.equalsIgnoreCase("duplicate")){
					
					
//					 startActivity(new Intent(getApplicationContext(),Register.class));
					 Toast.makeText(getApplicationContext(), "Username already Exist...", Toast.LENGTH_LONG).show();
					 
				}
				else
				{    				 
//					startActivity(new Intent(getApplicationContext(),Register.class));

					Toast.makeText(getApplicationContext(), " failed.TRY AGAIN!!", Toast.LENGTH_LONG).show();
				}
				
			} catch (Exception e) {
				// TODO: handle exception
				e.printStackTrace();
				  Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
			}
			
			
		}
		public void onBackPressed() 
		{
			// TODO Auto-generated method stub
			super.onBackPressed();
			Intent b=new Intent(getApplicationContext(),Login.class);			
			startActivity(b);
		}

}
