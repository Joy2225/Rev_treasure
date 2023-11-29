import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.security.spec.InvalidKeySpecException;
import java.util.Base64;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.DESKeySpec;
import javax.naming.Context;

public class Flagseven {
    public static void main(String[] args) {

        int editText8 = 0x7f0800ad;


         EditText editText = (EditText) findViewById(editText8);
         C2724g.m882d(editText, "editText8");
        String obj = editText.getText().toString();
        //EditText editText2 = (EditText) findViewById(R.id.editText7);
        //C2724g.m882d(editText2, "editText7");
        String obj2 = editText2.getText().toString();
        ApplicationC1492j applicationC1492j = new ApplicationC1492j();
        String m4064c = applicationC1492j.m4064c("flagSevenEncrypted", "");
        String m4064c2 = applicationC1492j.m4064c("flagSevenPasswordEncrypted", "");
        if (!C2724g.m885a(obj, m4064c) || !C2724g.m885a(obj2, m4064c2)) {
            Toast.makeText(this, "Try again! :D", 0).show();
            return;
        }
        FlagsOverview.f4480H = true;
        ApplicationC1492j applicationC1492j2 = new ApplicationC1492j();
        Context applicationContext = getApplicationContext();
        C2724g.m882d(applicationContext, "applicationContext");
        applicationC1492j2.m4065b(applicationContext, "flagSevenButtonColor", true);
        m4108F();
    }
}
