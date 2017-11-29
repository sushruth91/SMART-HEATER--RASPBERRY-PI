package com.example.anik4.caproject;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.HashMap;
import java.util.Map;

public class TempClass {

    public int val=0;

    public TempClass() {
        // Default constructor required for calls to DataSnapshot.getValue(User.class)
    }

    public TempClass(int val) {
        this.val = val;
    }

    public int getVal() {
        return val;
    }

    public void setVal(int val) {
        this.val = val;
    }
}