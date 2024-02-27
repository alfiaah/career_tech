package com.example.personalityprediction;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Bundle;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.Toast;

import org.json.JSONObject;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;

public class Requestforjob extends AppCompatActivity {

    private int PICK_PDF_REQUEST = 1;

    public static byte[] byteArray;
    //storage permission code
    private static final int STORAGE_PERMISSION_CODE = 123;

    //Uri to store the image uri
    private Uri filePath;
    String q;
    String data;

    private static final int FILE_SELECT_CODE = 0;

    Button b1,b2;
    ImageButton ib;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_requestforjob);

        try
        {
            if(android.os.Build.VERSION.SDK_INT>9)
            {
                StrictMode.ThreadPolicy policy=new StrictMode.ThreadPolicy.Builder().permitAll().build();
                StrictMode.setThreadPolicy(policy);
            }
        }
        catch (Exception e)
        {
            // TODO: handle exception
        }

        b1=(Button)findViewById(R.id.button);
        b2=(Button)findViewById(R.id.button5);

        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                showFileChooser();
            }
        });

        b2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                uploadFile();
            }
        });
    }
    private void showFileChooser() {
        Intent intent = new Intent();
        intent.setType("*/*");
        intent.setAction(Intent.ACTION_GET_CONTENT);
        intent.addCategory(Intent.CATEGORY_OPENABLE);
        startActivityForResult(Intent.createChooser(intent, "Select Pdf"), PICK_PDF_REQUEST);
//        Toast.makeText(this, "Please move your .pdf file to internal storage and retry", Toast.LENGTH_LONG).show();

    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == PICK_PDF_REQUEST && resultCode == RESULT_OK && data != null && data.getData() != null) {
            filePath = data.getData();
            Toast.makeText(getApplicationContext(),"onfileg"+filePath, Toast.LENGTH_LONG).show();
        }
    }



    private void uploadFile()
    {
        Toast.makeText(getApplicationContext(),"fffg"+filePath, Toast.LENGTH_LONG).show();
        String path = FilePath.getPath(this, filePath);
        Toast.makeText(getApplicationContext(),"Dhg"+path, Toast.LENGTH_LONG).show();
        if (path == null) {
            Toast.makeText(this, "Please move your .pdf file to internal storage and retry", Toast.LENGTH_LONG).show();
        } else {
            //Uploading code
            try {
                //Converting Bitmap to String
                File f=new File(path);
                byteArray = null;
                try
                {
                    InputStream inputStream = new FileInputStream(f);
                    ByteArrayOutputStream bos = new ByteArrayOutputStream();
                    byte[] b = new byte[(int)f.length()];
                    int bytesRead =0;

                    while ((bytesRead = inputStream.read(b)) != -1)
                    {
                        bos.write(b, 0, bytesRead);
                    }
                    byteArray = bos.toByteArray();
                }
                catch (Exception e)
                {
                }
//                encodedFile = Base64.encodeToString(byteArray, Base64.NO_WRAP);
                Toast.makeText(getApplicationContext(), "Len : " + byteArray.length, Toast.LENGTH_LONG).show();


                uploadData();

            } catch (Exception exc) {
                Toast.makeText(this, exc.getMessage(), Toast.LENGTH_SHORT).show();
            }
        }

//
    }

    private void uploadData() {

        try {
             q="http://"+IPSetting.ip+"/api/studentadduploadassignments/";
            FileUpload client = new FileUpload(q);
            client.connectForMultipart();



            client.addFormPart("logid",Login.logid);
            client.addFormPart("aid", UserViewjobs.jids);
            client.addFilePart("image", "abc.pdf", byteArray);

            //   client.addFilePart("image", "abc.jpg", bitmapdata);
            client.finishMultipart();
            data = client.getResponse();
            Log.d("lllllllll", data);
            JSONObject ob = new JSONObject(data);
//            JSONArray ar=new JSONArray(data);
            if (ob.getString("status").equals("success")) {
                Toast.makeText(getApplicationContext(), "Registered.!", Toast.LENGTH_LONG).show();
//                pb_loading.setVisibility(View.GONE);

                startActivity(new Intent(getApplicationContext(), User_Home.class));
            }
            else{
                Toast.makeText(getApplicationContext(), "Already Applied", Toast.LENGTH_LONG).show();
            }

            Log.d("response=======", data);
        } catch (Exception e)
        {
            Toast.makeText(getApplicationContext(), "Exception 123 : " + e, Toast.LENGTH_LONG).show();
            Log.d("jjj", e.toString());
        }
    }


}