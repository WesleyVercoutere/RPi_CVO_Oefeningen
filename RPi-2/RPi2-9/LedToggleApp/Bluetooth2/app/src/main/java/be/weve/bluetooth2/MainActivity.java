package be.weve.bluetooth2;

import androidx.appcompat.app.AppCompatActivity;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.content.Intent;
import android.os.Bundle;
import android.view.MotionEvent;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import java.io.IOException;
import java.io.OutputStream;
import java.util.Set;
import java.util.UUID;

public class MainActivity extends AppCompatActivity {

    private final String DEVICE_ADDRESS = "20:20:05:18:47:40"; //MAC Address of Bluetooth Module
    private final UUID PORT_UUID = UUID.fromString("00001101-0000-1000-8000-00805f9b34fb");

    private BluetoothDevice device;
    private BluetoothSocket socket;
    private OutputStream outputStream;

    private Button btn_redLed;
    private Button btn_connect;

    private String command; //string variable that will store value to be transmitted to the bluetooth module

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btn_redLed = (Button) findViewById(R.id.btnRedLed);
        btn_connect = (Button) findViewById(R.id.btnConnect);

        setListeners();
        initBluetooth();
    }

    private void setListeners() {
        btn_redLed.setOnClickListener(view -> {
            command = "red";

            try {
                outputStream.write(command.getBytes());
            }
            catch (Exception e) {
                e.printStackTrace();
            }
        });

        btn_connect.setOnClickListener(view -> {

            if (initBluetooth()) {
                connectBluetooth();
            }

        });
    }

    private boolean initBluetooth() {

        boolean found = false;

        BluetoothAdapter bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();

        if(bluetoothAdapter == null) //Checks if the device supports bluetooth
        {
            Toast.makeText(getApplicationContext(), "Device doesn't support bluetooth", Toast.LENGTH_SHORT).show();
        }

        if(!bluetoothAdapter.isEnabled()) //Checks if bluetooth is enabled. If not, the program will ask permission from the user to enable it
        {
            Intent enableAdapter = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
            startActivityForResult(enableAdapter,0);

            try
            {
                Thread.sleep(1000);
            }
            catch(InterruptedException e)
            {
                e.printStackTrace();
            }
        }

        Set<BluetoothDevice> bondedDevices = bluetoothAdapter.getBondedDevices();

        if(bondedDevices.isEmpty()) //Checks for paired bluetooth devices
        {
            Toast.makeText(getApplicationContext(), "Please pair the device first", Toast.LENGTH_SHORT).show();
        }
        else
        {
            for(BluetoothDevice iterator : bondedDevices)
            {
                if(iterator.getAddress().equals(DEVICE_ADDRESS))
                {
                    device = iterator;
                    found = true;
                    break;
                }
            }
        }

        return found;
    }

    public boolean connectBluetooth() {
        boolean connected = true;

        try {
            socket = device.createRfcommSocketToServiceRecord(PORT_UUID); //Creates a socket to handle the outgoing connection
            socket.connect();

            Toast.makeText(getApplicationContext(),
                    "Connection to bluetooth device successful", Toast.LENGTH_LONG).show();
        }
        catch(IOException e) {
            e.printStackTrace();
            connected = false;
        }

        if(connected) {
            try {
                outputStream = socket.getOutputStream(); //gets the output stream of the socket
            }
            catch(IOException e) {
                e.printStackTrace();
            }
        }

        return connected;
    }




}


/*

import android.annotation.SuppressLint;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothServerSocket;
import android.bluetooth.BluetoothSocket;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.Set;
import java.util.UUID;

public class multiplayerConnect extends AppCompatActivity {

public static final int REQUEST_ENABLE_BT=1;
ListView lv_paired_devices;
Set<BluetoothDevice> set_pairedDevices;
ArrayAdapter adapter_paired_devices;
BluetoothAdapter bluetoothAdapter;
public static final UUID MY_UUID = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB");
public static final int MESSAGE_READ=0;
public static final int MESSAGE_WRITE=1;
public static final int CONNECTING=2;
public static final int CONNECTED=3;
public static final int NO_SOCKET_FOUND=4;


String bluetooth_message="00";




@SuppressLint("HandlerLeak")
Handler mHandler=new Handler()
{
    @Override
    public void handleMessage(Message msg_type) {
        super.handleMessage(msg_type);

        switch (msg_type.what){
            case MESSAGE_READ:

                byte[] readbuf=(byte[])msg_type.obj;
                String string_recieved=new String(readbuf);

                //do some task based on recieved string

                break;
            case MESSAGE_WRITE:

                if(msg_type.obj!=null){
                    ConnectedThread connectedThread=new ConnectedThread((BluetoothSocket)msg_type.obj);
                    connectedThread.write(bluetooth_message.getBytes());

                }
                break;

            case CONNECTED:
                Toast.makeText(getApplicationContext(),"Connected",Toast.LENGTH_SHORT).show();
                break;

            case CONNECTING:
                Toast.makeText(getApplicationContext(),"Connecting...",Toast.LENGTH_SHORT).show();
                break;

            case NO_SOCKET_FOUND:
                Toast.makeText(getApplicationContext(),"No socket found",Toast.LENGTH_SHORT).show();
                break;
        }
    }
};



@Override
protected void onCreate(@Nullable Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.multiplayer_bluetooth);
    initialize_layout();
    initialize_bluetooth();
    start_accepting_connection();
    initialize_clicks();

}

public void start_accepting_connection()
{
    //call this on button click as suited by you

    AcceptThread acceptThread = new AcceptThread();
    acceptThread.start();
    Toast.makeText(getApplicationContext(),"accepting",Toast.LENGTH_SHORT).show();
}
public void initialize_clicks()
{
    lv_paired_devices.setOnItemClickListener(new AdapterView.OnItemClickListener() {
        @Override
        public void onItemClick(AdapterView<?> parent, View view, int position, long id)
        {
            Object[] objects = set_pairedDevices.toArray();
            BluetoothDevice device = (BluetoothDevice) objects[position];

            ConnectThread connectThread = new ConnectThread(device);
            connectThread.start();

            Toast.makeText(getApplicationContext(),"device choosen "+device.getName(),Toast.LENGTH_SHORT).show();
        }
    });
}

public void initialize_layout()
{
    lv_paired_devices = (ListView)findViewById(R.id.lv_paired_devices);
    adapter_paired_devices = new ArrayAdapter(getApplicationContext(),R.layout.support_simple_spinner_dropdown_item);
    lv_paired_devices.setAdapter(adapter_paired_devices);
}

public void initialize_bluetooth()
{
    bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
    if (bluetoothAdapter == null) {
        // Device doesn't support Bluetooth
        Toast.makeText(getApplicationContext(),"Your Device doesn't support bluetooth. you can play as Single player",Toast.LENGTH_SHORT).show();
        finish();
    }

    //Add these permisions before
//        <uses-permission android:name="android.permission.BLUETOOTH" />
//        <uses-permission android:name="android.permission.BLUETOOTH_ADMIN" />
//        <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
//        <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>

    if (!bluetoothAdapter.isEnabled()) {
        Intent enableBtIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
        startActivityForResult(enableBtIntent, REQUEST_ENABLE_BT);
    }

    else {
        set_pairedDevices = bluetoothAdapter.getBondedDevices();

        if (set_pairedDevices.size() > 0) {

            for (BluetoothDevice device : set_pairedDevices) {
                String deviceName = device.getName();
                String deviceHardwareAddress = device.getAddress(); // MAC address

                adapter_paired_devices.add(device.getName() + "\n" + device.getAddress());
            }
        }
    }
}


public class AcceptThread extends Thread
{
    private final BluetoothServerSocket serverSocket;

    public AcceptThread() {
        BluetoothServerSocket tmp = null;
        try {
            // MY_UUID is the app's UUID string, also used by the client code
            tmp = bluetoothAdapter.listenUsingRfcommWithServiceRecord("NAME",MY_UUID);
        } catch (IOException e) { }
        serverSocket = tmp;
    }

    public void run() {
        BluetoothSocket socket = null;
        // Keep listening until exception occurs or a socket is returned
        while (true) {
            try {
                socket = serverSocket.accept();
            } catch (IOException e) {
                break;
            }

            // If a connection was accepted
            if (socket != null)
            {
                // Do work to manage the connection (in a separate thread)
                mHandler.obtainMessage(CONNECTED).sendToTarget();
            }
        }
    }
}


private class ConnectThread extends Thread {
    private final BluetoothSocket mmSocket;
    private final BluetoothDevice mmDevice;

    public ConnectThread(BluetoothDevice device) {
        // Use a temporary object that is later assigned to mmSocket,
        // because mmSocket is final
        BluetoothSocket tmp = null;
        mmDevice = device;

        // Get a BluetoothSocket to connect with the given BluetoothDevice
        try {
            // MY_UUID is the app's UUID string, also used by the server code
            tmp = device.createRfcommSocketToServiceRecord(MY_UUID);
        } catch (IOException e) { }
        mmSocket = tmp;
    }

    public void run() {
        // Cancel discovery because it will slow down the connection
        bluetoothAdapter.cancelDiscovery();

        try {
            // Connect the device through the socket. This will block
            // until it succeeds or throws an exception
            mHandler.obtainMessage(CONNECTING).sendToTarget();

            mmSocket.connect();
        } catch (IOException connectException) {
            // Unable to connect; close the socket and get out
            try {
                mmSocket.close();
            } catch (IOException closeException) { }
            return;
        }

        // Do work to manage the connection (in a separate thread)
//            bluetooth_message = "Initial message"
//            mHandler.obtainMessage(MESSAGE_WRITE,mmSocket).sendToTarget();
    }

    /** Will cancel an in-progress connection, and close the socket */
public void cancel() {
    try {
        mmSocket.close();
    } catch (IOException e) { }
}
}
private class ConnectedThread extends Thread {

    private final BluetoothSocket mmSocket;
    private final InputStream mmInStream;
    private final OutputStream mmOutStream;

    public ConnectedThread(BluetoothSocket socket) {
        mmSocket = socket;
        InputStream tmpIn = null;
        OutputStream tmpOut = null;

        // Get the input and output streams, using temp objects because
        // member streams are final
        try {
            tmpIn = socket.getInputStream();
            tmpOut = socket.getOutputStream();
        } catch (IOException e) { }

        mmInStream = tmpIn;
        mmOutStream = tmpOut;
    }

    public void run() {
        byte[] buffer = new byte[2];  // buffer store for the stream
        int bytes; // bytes returned from read()

        // Keep listening to the InputStream until an exception occurs
        while (true) {
            try {
                // Read from the InputStream
                bytes = mmInStream.read(buffer);
                // Send the obtained bytes to the UI activity
                mHandler.obtainMessage(MESSAGE_READ, bytes, -1, buffer).sendToTarget();

            } catch (IOException e) {
                break;
            }
        }
    }

    /* Call this from the main activity to send data to the remote device */
    public void write(byte[] bytes) {
        try {
            mmOutStream.write(bytes);
        } catch (IOException e) { }
    }

    /* Call this from the main activity to shutdown the connection */
    public void cancel() {
        try {
            mmSocket.close();
        } catch (IOException e) { }
    }
}
}


 */