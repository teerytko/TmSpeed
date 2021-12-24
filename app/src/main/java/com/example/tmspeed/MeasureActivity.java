package com.example.tmspeed;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;

public class MeasureActivity extends AppCompatActivity {

    private static final String TAG = "TMSpeed";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_measure);
        Intent intent = getIntent();
        float distance = intent.getFloatExtra("distance", 0);
        Log.i(TAG, "Started: distance "+distance);
    }
}