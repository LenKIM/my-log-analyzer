import hu.akarnokd.rxjava2.math.MathObservable;
import io.reactivex.Observable;
import io.reactivex.ObservableSource;
import io.reactivex.Observer;
import org.junit.Test;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;

public class LogAnalyerFunction01 {
    /**
     * 파일 불러오기 RxJava
     */
    @Test
    public void function01() {
        long start = System.currentTimeMillis();
        Observable<LogWithTime> observable = Observable.defer(() -> new FileObservableSource("/Users/len/Desktop/logdata/ap1.daouoffice.com_access_2018-08-24.log"))
                .map(s -> {
                    ArrayList<String> abc = parseLine(s);
                    Float responseTime = Float.parseFloat(abc.get(13));
                    String restApi = abc.get(6);
                    return new LogWithTime(restApi, responseTime);
                });


        Observable<LogWithTime> observable2 = Observable.defer(() -> new FileObservableSource("/Users/len/Desktop/logdata/ap2.daouoffice.com_access_2018-08-24.log"))
                .map(s -> {
                    ArrayList<String> abc = parseLine(s);
                    Float responseTime = Float.parseFloat(abc.get(13));
                    String restApi = abc.get(6);
                    return new LogWithTime(restApi, responseTime);
                });


        Observable<LogWithTime> observable3 = Observable.defer(() -> new FileObservableSource("/Users/len/Desktop/logdata/ap3.daouoffice.com_access_2018-08-24.log"))
                .map(s -> {
                    ArrayList<String> abc = parseLine(s);
                    Float responseTime = Float.parseFloat(abc.get(13));
                    String restApi = abc.get(6);
                    return new LogWithTime(restApi, responseTime);
                });


        getMaxValue(observable).subscribe(System.out::println);
        getMaxValue(observable2).subscribe(System.out::println);
        getMaxValue(observable3).subscribe(System.out::println);
        long end = System.currentTimeMillis();
        System.out.println("실행시간 " + (end - start) / 1000 + '초');

    }
    private Observable<LogWithTime> getMaxValue(Observable<LogWithTime> observable3) {
        return MathObservable.max(observable3, (o1, o2) -> {
            float a = o1.getTime();
            float b = o2.getTime();
            if (a - b > 0) return 1;
            if (a - b < 0) return -1;
            return 0;
        });
    }


    private ArrayList<String> parseLine(String line) {

        ArrayList<String> a = new ArrayList<>();

        int splitIdx;
        String nextStr = line; // 이미 파싱이 끝난 문자열을 제외하고 subString한 문자열을 담는 변수 // 초기값은 line


        for (int i = 0; i < 14; i++) {
            splitIdx = parseComponent(nextStr);

            if (splitIdx == 0) {
                a.add(nextStr);
                break;
            }
            a.add(nextStr.substring(0, splitIdx));
            nextStr = nextStr.substring(splitIdx);
        }
        return a;
    }

    class LogWithTime {

        LogWithTime(String restApi, float time) {
            this.restApi = restApi;
            this.time = time;
        }

        String restApi;
        float time;

        public void setTime(float time) {
            this.time = time;
        }

        float getTime() {
            return time;
        }

        public void setRestApi(String restApi) {
            this.restApi = restApi;
        }

        public String getRestApi() {
            return restApi;
        }

        @Override
        public String toString() {
            return "LogWithTime{" +
                    "restApi='" + restApi + '\'' +
                    ", time=" + time +
                    '}';
        }
    }

    private int parseComponent(String input) {

        int splitIdx;
        String splitedStr;

        String firstChar = input.substring(0, 1); // 문자열의 맨 첫 문자

        // 특정 기준으로 파싱하기 // " 또는 [ 또는 ( 또는 공백( )
        if (firstChar.equals("\"")) {
            // 시작이 따옴표일 때 // 공백 기준으로 자르지 않고 input에서 따옴표+공백(" )을 찾아 자른다.
            splitIdx = input.indexOf("\" ");

            // indexOf메서드에서 해당 문자열을 찾지 못한 경우 -1이 반환된다.
            if (splitIdx != -1) {
                splitedStr = input.substring(0, splitIdx + 1);
            } else {
                splitedStr = input;
            }

            splitIdx = splitIdx + 2;

        } else if (firstChar.equals("[")) {
            // 시작이 대괄호일 때

            splitIdx = input.indexOf("]");
            if (splitIdx != -1) {
                splitedStr = input.substring(1, splitIdx);
            } else {
                splitedStr = input;
            }

            splitIdx = splitIdx + 2;
        } else if (firstChar.equals("(")) {
            // 시작이 괄호일 때

            splitIdx = input.indexOf(")");
            if (splitIdx != -1) {
                splitedStr = input.substring(1, splitIdx);
            } else {
                splitedStr = input;
            }

            splitIdx = splitIdx + 2;
        } else {
            // 시작이 단순 문자일 때
            splitIdx = input.indexOf(" ");
            splitedStr = input;

            splitIdx = splitIdx + 1;
        }

        return splitIdx;
    }

    static class FileObservableSource implements ObservableSource<String> {

        private final String filename;

        FileObservableSource(String filename) {
            this.filename = filename;
        }

        @Override
        public void subscribe(Observer<? super String> observer) {
            try {
                Files.lines(Paths.get(filename)).forEach(observer::onNext);
                observer.onComplete();
            } catch (IOException e) {
                observer.onError(e);
            }
        }
    }
}

//        Observable.zip(getMaxValue(observable),
//                getMaxValue(observable2),
//                getMaxValue(observable3),
//                (logWithTime, logWithTime2, logWithTime3) -> {
//                    LogWithTime temp;
//                    if (logWithTime.getTime() > logWithTime2.getTime()) {
//                        temp = logWithTime;
//                    } else {
//                        temp = logWithTime2;
//                    }
//                    if (logWithTime3.getTime() > temp.getTime()) {
//                        return logWithTime3;
//                    } else {
//                        return temp;
//                    }
//                }
//
//        ).subscribe(System.out::println);