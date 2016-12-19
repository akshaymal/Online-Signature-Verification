package com.example.akshay.signatureapp4;


import android.support.design.widget.FloatingActionButton;
import android.app.FragmentManager;
import android.app.Fragment;
import android.app.FragmentTransaction;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;

import static android.R.attr.id;

public class MainActivity extends AppCompatActivity {

    FloatingActionButton fabplus, fabverify,fabincognito, fabdelete;
    Animation fabopen,fabclose,fabclockwise,fabanticlockwise,fabopenplus,fabcloseplus;
    boolean isopen = false;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        fabplus = (FloatingActionButton)findViewById(R.id.fab_plus);
        fabverify = (FloatingActionButton)findViewById(R.id.fab_verify);
        fabincognito = (FloatingActionButton)findViewById(R.id.fab_incognito);
        fabdelete = (FloatingActionButton)findViewById(R.id.fabclose);

        fabopen = AnimationUtils.loadAnimation(getApplicationContext(),R.anim.fab_open);
        fabclose = AnimationUtils.loadAnimation(getApplicationContext(),R.anim.fab_close);
        fabopenplus = AnimationUtils.loadAnimation(getApplicationContext(),R.anim.fab_openplus);
        fabcloseplus = AnimationUtils.loadAnimation(getApplicationContext(),R.anim.fab_closeplus);
        fabclockwise = AnimationUtils.loadAnimation(getApplicationContext(),R.anim.rotate_clockwise);
        fabanticlockwise = AnimationUtils.loadAnimation(getApplicationContext(),R.anim.rotate_anticlockwise);


        fabplus.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                if (isopen)
                {
                    fabincognito.startAnimation(fabclose);
                    fabverify.startAnimation(fabcloseplus);
                    fabplus.startAnimation(fabanticlockwise);
                    fabincognito.setClickable(false);
                    fabverify.setClickable(false);
                    isopen = false;

                }
                else
                {
                    fabincognito.startAnimation(fabopen);
                    fabverify.startAnimation(fabopenplus);
                    fabplus.startAnimation(fabclockwise);
                    fabincognito.setClickable(true);
                    fabverify.setClickable(true);
                    isopen = true;
                }
            }

        });

        fabdelete.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                recreate();
    }

        });
    }
}

/*
*
* */
