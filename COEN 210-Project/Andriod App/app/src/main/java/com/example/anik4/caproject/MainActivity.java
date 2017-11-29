package com.example.anik4.caproject;

import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.ToggleButton;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class MainActivity extends AppCompatActivity  {



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        //start
        final TextView tem=(TextView)findViewById(R.id.textView4);
        final TextView hum=(TextView)findViewById(R.id.textView5);
        final TextView alt=(TextView)findViewById(R.id.textView6);
        final TextView pre=(TextView)findViewById(R.id.textView7);

        //final Button set_temp= (Button) findViewById(R.id.button2);
        //final EditText temp_val=(EditText) findViewById(R.id.et1);
        final Switch s1=(Switch) findViewById(R.id.switch1);
        final DatabaseReference mDatabase = FirebaseDatabase.getInstance().getReference();
        //final String t= mDatabase.push().getKey();
        final TempClass tempClass1= new TempClass();


        s1.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                if(s1.isChecked()){

                    //int val= Integer.parseInt(temp_val.getText().toString());

                    tempClass1.setVal(1);
                    String val=Integer.toString(tempClass1.getVal());
                    String val1="\""+val+"\"";
                    mDatabase.child("System Status").setValue(val);
                    Toast.makeText(getApplicationContext(),"On "+val,Toast.LENGTH_LONG).show();
                }
                else {

                    //int val= Integer.parseInt(temp_val.getText().toString());

                    tempClass1.setVal(0);
                    String val=Integer.toString(tempClass1.getVal());
                    String val1="\""+val+"\"";
                    mDatabase.child("System Status").setValue(val);
                    Toast.makeText(getApplicationContext(),"Off "+ val,Toast.LENGTH_LONG).show();

                }


            }
        });

        mDatabase.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                String s1= dataSnapshot.child("Coffee Temperature").getValue(String.class);
                String s2= dataSnapshot.child("Sensor Readings").child("Humidity").getValue(String.class);
                String s3= dataSnapshot.child("Sensor Readings").child("Pressure").getValue(String.class);
                String s4= dataSnapshot.child("Sensor Readings").child("Altitude").getValue(String.class);
                tem.setText(s1);
                hum.setText(s2);
                alt.setText(s3);
                pre.setText(s4);
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {

            }
        });




        /*set_temp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                int val= Integer.parseInt(temp_val.getText().toString());

                    Toast.makeText(getApplicationContext(),"value is "+val,Toast.LENGTH_LONG).show();
                    TempClass tempClass= new TempClass(temperature);
                    mDatabase.child(t).setValue(tempClass);
                    //mDatabase.child(t).setValue(pressure);
                    //mDatabase.setValue(humidity);
            }
        });*/




        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });


    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
