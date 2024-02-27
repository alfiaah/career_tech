package com.example.personalityprediction;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class UserViewjobs extends AppCompatActivity implements AdapterView.OnItemClickListener,JsonResponse {

    ListView lv1;
    String [] jid,cid,job,detail,lastdate,val;
    public static String cids,jids;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_viewjobs);

        lv1=(ListView)findViewById(R.id.lvjobs);

        lv1.setOnItemClickListener(this);

        JsonReq JR=new JsonReq();
        JR.json_response=(JsonResponse) UserViewjobs.this;
        String q = "/UserViewJobs";
        q=q.replace(" ","%20");
        JR.execute(q);


    }

    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {

        jids=jid[position];
        cids=cid[position];

        final CharSequence[] items = {"View Comapny","Request for Job","Cancel"};

        AlertDialog.Builder builder = new AlertDialog.Builder(UserViewjobs.this);
        // builder.setTitle("Add Photo!");
        builder.setItems(items, new DialogInterface.OnClickListener()
        {
            @Override
            public void onClick(DialogInterface dialog, int item) {
                if (items[item].equals("View Comapny"))
                {
                    startActivity(new Intent(getApplicationContext(),UserViewCompany.class));
                }
                else if (items[item].equals("Request for Job"))
                {
                    startActivity(new Intent(getApplicationContext(),Requestforjob.class));
                }

                else if (items[item].equals("Cancel")) {
                    dialog.dismiss();
                }
            }

        });
        builder.show();


    }

    @Override
    public void response(JSONObject jo) {
        try {

            String method=jo.getString("method");
            if(method.equalsIgnoreCase("UserViewJobs")){
                String status=jo.getString("status");
                Log.d("pearl",status);
                Toast.makeText(getApplicationContext(),status, Toast.LENGTH_SHORT).show();
                if(status.equalsIgnoreCase("success")){

                    JSONArray ja1=(JSONArray)jo.getJSONArray("data");

                    jid=new String[ja1.length()];
                    cid=new String[ja1.length()];
                    job=new String[ja1.length()];
                    detail=new String[ja1.length()];
                    lastdate=new String[ja1.length()];



                    val=new String[ja1.length()];



                    for(int i = 0;i<ja1.length();i++)
                    {


                        jid[i]=ja1.getJSONObject(i).getString("job_id");
                        cid[i]=ja1.getJSONObject(i).getString("company_id");
                        job[i]=ja1.getJSONObject(i).getString("job");
                        detail[i]=ja1.getJSONObject(i).getString("details");
                        lastdate[i]=ja1.getJSONObject(i).getString("last_date");


//                        Toast.makeText(getApplicationContext(),val[i], Toast.LENGTH_SHORT).show();
                        val[i]="Job: "+job[i]+"\nDetail:  "+detail[i]+"\nLast Date:  "+lastdate[i];

                    }
                    ArrayAdapter<String> ar=new ArrayAdapter<String>(getApplicationContext(),android.R.layout.simple_list_item_1,val);
                    lv1.setAdapter(ar);



                }

                else {
                    Toast.makeText(getApplicationContext(), "no data", Toast.LENGTH_LONG).show();

                }
            }
//			if(method.equalsIgnoreCase("buyprod"))
//			{
//				String status=jo.getString("status");
//				Toast.makeText(getApplicationContext(),status, Toast.LENGTH_LONG).show();
//				if(status.equalsIgnoreCase("success"))
//				{
//					Toast.makeText(getApplicationContext(),"Your order is submitted!", Toast.LENGTH_LONG).show();
//				}
//				else{
//					Toast.makeText(getApplicationContext(),"Your order is not submitted", Toast.LENGTH_LONG).show();
//				}
//			}
        }catch (Exception e)
        {
            // TODO: handle exception

            Toast.makeText(getApplicationContext(),e.toString(), Toast.LENGTH_LONG).show();
        }



    }
}