package com.example.akshay.signatureapp4;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Path;
import android.os.Environment;
import android.support.design.widget.FloatingActionButton;
//import android.support.v4.app.Fragment;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.util.AttributeSet;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.MotionEvent;
import android.support.design.widget.FloatingActionButton;
import android.app.FragmentManager;
import android.app.Fragment;
import android.app.FragmentTransaction;
import android.view.ViewTreeObserver;
import android.widget.Button;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;

import static android.R.attr.id;

/**
 * Created by akshay on 11/5/16.
 */

public class topfragment extends Fragment{

    int check=0;

    public Path path = new Path();
    Context c;
    String finaldata = "X, Y, TStamp, Pres., EndPts\n" + "DataSize: 698\n";


    public class TouchEventView1 extends View {

        private Paint paint = new Paint();
        //public Path path = new Path();

        public TouchEventView1 (Context ctx, AttributeSet attrs)
        {
            super(ctx,attrs);
            c = ctx;
            paint.setAntiAlias(true);
            paint.setColor(Color.BLACK);
            paint.setStrokeJoin(Paint.Join.ROUND);
            paint.setStyle(Paint.Style.STROKE);
            paint.setStrokeWidth(10f);
            this.setBackgroundColor(Color.parseColor("#eeeeee"));

        }

        public void reseter()
        {
            path.reset();
        }



        @Override
        protected void onDraw (Canvas canvas)
        {
            canvas.drawPath(path,paint);
        }

        @Override
        public boolean onTouchEvent(MotionEvent event)
        {
            String data;
            int xpos;
            int ypos;
            float t = System.nanoTime()/10000000;
            int time = (int)t;
            //System.out.println(data);
            /*
            *
            * if (check==1) {
                check = 2;
                data = data + Integer.toString(1) + "\n";
            }
            else
            {
                data = data + Integer.toString(0) + "\n";
            }
            System.out.println(data);*/

            /*finaldata = finaldata + data;

            try {
                BufferedWriter fos = new BufferedWriter(new FileWriter(Environment.getExternalStorageDirectory().getAbsolutePath() +"/"+"signaturecontent.txt"));
                fos.write(finaldata.trim());
                fos.close();
            } catch (Exception e) {

            }*/

            //System.out.println(data);


            switch(event.getAction())
            {
                case MotionEvent.ACTION_DOWN:
                    xpos = (int)event.getX();
                    ypos = (int)event.getY();
                    data = Integer.toString(xpos) + " " + Integer.toString(ypos) + " " + Integer.toString(time)  + " " + Integer.toString(0) + " "  + Integer.toString(0) + "\n";
                    finaldata = finaldata + data;
                    try {
                        BufferedWriter fos = new BufferedWriter(new FileWriter(Environment.getExternalStorageDirectory().getAbsolutePath() +"/"+"signaturecontent.sig"));
                        fos.write(finaldata.trim());
                        fos.close();
                    } catch (Exception e) {

                    }
                    path.moveTo(xpos, ypos);
                    return true;

                case MotionEvent.ACTION_MOVE:
                    xpos = (int)event.getX();
                    ypos = (int)event.getY();
                    data = Integer.toString(xpos) + " " + Integer.toString(ypos) + " " + Integer.toString(time)  + " " + Integer.toString(0) + " "  + Integer.toString(0) + "\n";
                    finaldata = finaldata + data;
                    try {
                        BufferedWriter fos = new BufferedWriter(new FileWriter(Environment.getExternalStorageDirectory().getAbsolutePath() +"/"+"signaturecontent.sig"));
                        fos.write(finaldata.trim());
                        fos.close();
                    } catch (Exception e) {

                    }
                    path.lineTo(xpos, ypos);
                    invalidate();
                    return true;

                case MotionEvent.ACTION_UP:
                    xpos = (int)event.getX();
                    ypos = (int)event.getY();
                    data = Integer.toString(xpos) + " " + Integer.toString(ypos) + " " + Integer.toString(time)  + " " + Integer.toString(0) + " "  + Integer.toString(1) + "\n";
                    finaldata = finaldata + data;
                    try {
                        BufferedWriter fos = new BufferedWriter(new FileWriter(Environment.getExternalStorageDirectory().getAbsolutePath() +"/"+"signaturecontent.sig"));
                        fos.write(finaldata.trim());
                        fos.close();
                    } catch (Exception e) {

                    }
                    check = 1;
                    break;

                default:
                    return false;
            }
            return true;
            //return false;
        }


    }


    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.topfragment,container,false);
        return new TouchEventView1(this.getActivity(),null);
    }

    public String restart()
    {
        return finaldata;
    }
}
