package com.example.personalityprediction;

import org.json.JSONArray;
import org.json.JSONObject;


import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class Login extends Activity implements JsonResponse {
	EditText e1,e2;
	TextView t1;
    Button b1;
    String username , password;
    public static String logid,usertype;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_login);

		t1=(TextView)findViewById(R.id.textView5);
		e1=(EditText)findViewById(R.id.etuser);
		e2=(EditText)findViewById(R.id.etpass);
		b1=(Button)findViewById(R.id.btlogin);
		
//		startService(new Intent(getApplicationContext(),LocationService.class));
		

		
		t1.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View arg0) {
				// TODO Auto-generated method stub
				startActivity(new Intent(getApplicationContext(),UserRegister.class));
			}
		});
		
		
		b1.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View arg0) {
				// TODO Auto-generated method stub
				username=e1.getText().toString();
				password=e2.getText().toString();
//			   Toast.makeText(getApplicationContext(),username +" "+password+" ",Toast.LENGTH_LONG).show();
				if(username.equalsIgnoreCase(""))
				{
				  e1.setError("please enter username");
				  e1.setFocusable(true);
				}
				else if(password.equalsIgnoreCase(""))
				{
				  e2.setError("enter correct Password");
				  e2.setFocusable(true);
				}

				else{
					JsonReq JR=new JsonReq();
			        JR.json_response=(JsonResponse) Login.this;
			        String q = "/login?username="+username+"&password="+password;
			        q=q.replace(" ","%20");
			        JR.execute(q);
				}
				
			}
		}); 
	}


	

	@Override
	public void response(JSONObject jo) {
		// TODO Auto-generated method stub
		try {
			String status=jo.getString("status");
			Log.d("pearl",status);
			//Toast.makeText(getApplicationContext(),status, Toast.LENGTH_LONG).show();

			if(status.equalsIgnoreCase("success")){
				JSONArray ja1=(JSONArray)jo.getJSONArray("data");
				logid=ja1.getJSONObject(0).getString("login_id");
				usertype=ja1.getJSONObject(0).getString("usertype");
				
//				Editor e=sh.edit();
//				e.putString("log_id", logid);
//				e.commit();
				if(usertype.equals("user"))
				{
					 
						
			           Toast.makeText(getApplicationContext()," You are Login Successfully!...,",Toast.LENGTH_LONG).show();
			           startActivity(new Intent(getApplicationContext(),User_Home.class));

				}
				
             
			
			}	
			else {
				Toast.makeText(getApplicationContext(),"Login failed..!Please enter correct username or password ",Toast.LENGTH_LONG).show();
//				Intent i=new Intent(getApplicationContext(),MainLogin.class);
			startActivity(new Intent(getApplicationContext(),Login.class));
			}
				
			
		}catch (Exception e) {
			// TODO: handle exception
			
			  Toast.makeText(getApplicationContext(),e.toString(), Toast.LENGTH_LONG).show();
		}
		
		
	}
	public void onBackPressed() 
	{
		// TODO Auto-generated method stub
		super.onBackPressed();
		Intent b=new Intent(getApplicationContext(),IPSetting.class);			
		startActivity(b);
	}

}
