package com.example.tmspeed;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "TMSpeed";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        final EditText distance = (EditText) findViewById(R.id.editTextDistance);
        final Button button = (Button) findViewById(R.id.measure_start);
        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // your handler code here
                String distStr = String.valueOf(distance.getText());
                Float dist = Float.parseFloat(distStr);
                Log.i(TAG, "Measure start!");
                Intent myIntent = new Intent(MainActivity.this, MeasureActivity.class);
                myIntent.putExtra("distance", dist); //Optional parameters
                MainActivity.this.startActivity(myIntent);
            }
        });

    }

}